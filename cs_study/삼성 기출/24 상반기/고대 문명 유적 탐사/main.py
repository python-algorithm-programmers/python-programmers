from collections import deque
from pprint import pprint

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def rotate(arr, r, c):
    # 중심 좌표 기준으로 3 by 3으로 쪼개고 회전
    new_arr = []
    for y in range(r-1, r+2):
        new_line = []
        for x in range(c-1, c+2):
            new_line.append(arr[y][x])
        new_arr.append(new_line)

    rotate_new_arr = list(map(list, zip(*new_arr[::-1])))
    # 3 by 3 크기로 회전된것을 원래 것에 반영
    for y in range(r - 1, r + 2):
        for x in range(c - 1, c + 2):
            arr[y][x] = rotate_new_arr[y-(r-1)][x-(c-1)]
    return arr

def get_price(grand_map):
    visited = [[False] * 5 for _ in range(5)]
    out_dict = {}
    total = 0
    end_flag = [False]

    for r in range(5):
        for c in range(5):
            if not visited[r][c]:
                point = grand_map[r][c]
                id_key = f"{r}_{c}"
                if not out_dict.get(id_key):
                    out_dict[id_key] = []
                queue = deque([(r, c)])
                max_p = 0
                while queue:
                    start_y, start_x = queue.popleft()
                    out_dict[id_key].append((start_y, start_x))
                    visited[start_y][start_x] = True

                    # 최대 갯수 갱신
                    max_p += 1
                    for dy, dx in directions:
                        ny, nx = start_y + dy, start_x + dx
                        if 0 <= ny < 5 and 0 <= nx < 5 \
                                and point == grand_map[ny][nx] \
                                and not visited[ny][nx]:
                            queue.append((ny, nx))
                            visited[ny][nx] = True
                """조각 버퍼 삭제 여부 확인"""
                # 유물 조각 갯수가 3개 이상이 아니면 out_dict 삭제
                if max_p < 3:
                    del out_dict[id_key]

    """유물 삭제"""
    # 삭제해야될 조각들이 있다면 삭제
    if out_dict:
        dict_key = list(out_dict.keys())
        for key in dict_key:
            for out_r, out_c in out_dict[key]:
                grand_map[out_r][out_c] = 0
                total += 1

    return total, grand_map

def solution(grand_map, bonus_list, K, M):
    answer = []
    end_flag = [False]
    while K > 0:
        price = 0
        """
        [회전 + 최대 Price 찾기]
        - 3가지 중에 찾기
        - 회전각, price, 작은 순 중심 x, 중심 y
        """
        # 안쪽 좌표만 돌면서 최댓값이 어디인지를 찾아야함
        candidates = []
        for r in range(1, 4):
            for c in range(1, 4):
                for i in range(1, 4):
                    new_map = [arr[:] for arr in grand_map]
                    for _ in range(i):
                        new_map = rotate(new_map, r, c)
                    total, delete_map = get_price(new_map)
                    #print("r, c, rotate", r, c, i)
                    #pprint(delete_map)
                    if total > 0:
                        candidates.append((total, i, c, r, delete_map))

        if not candidates:
            break

        candidates.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
        total, _, _, _, delete_map = candidates[0]
        #print(candidates[0])

        # 탐색 반영
        price += total
        grand_map = delete_map
        #print("first_round_map")
        #pprint(grand_map)

        """
        [유물 조각 삭제]
        while True
            - 삭제 후 조각 채우기
                - 쓴 조각은 pop(0)으로 제외
            - 조각 채운 후 조각을 또 삭제할 수 있는 지 확인
            - 삭제할 수 없으면 종료, 채울 수 있으면 또 채움
        """
        #print(answer)
        while True:
            # 탐색하고 빈 것 확인하면 채워넣는 식
            can_switch = False
            for c in range(5):
                for r in range(4, -1, -1):
                    if grand_map[r][c] == 0:
                        if not can_switch:
                            can_switch = True
                        input_bonus = bonus_list.pop(0)
                        grand_map[r][c] = input_bonus

            if not can_switch:
               break

            #print("after_input map")
            #pprint(grand_map)

            # 채워놓고 탐색해서 같은 거 찾으면 또 지우기
            first_map = [arr[:] for arr in grand_map]
            add_point, delete_map = get_price(grand_map)
            grand_map = delete_map
            price += add_point

            #print("after_delete map")
            #pprint(grand_map)
            if first_map == grand_map:
                end_flag[0] = True
                break

        if price > 0:
            answer.append(price)
        #print("final_map")
        #pprint(grand_map)
        K -= 1
        #print("count_down", K)
        #pprint(delete_map)
    return answer


if __name__ == "__main__":
    K, M = map(int, input().split())
    grand_map = []
    for _ in range(5):
        grand_map.append(list(map(int, input().split())))

    bonus_list = list(map(int, input().split()))
    ans = solution(grand_map, bonus_list, K, M)
    print(*ans)