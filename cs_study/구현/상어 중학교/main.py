from collections import deque
from pprint import pprint


def gravity(block_map):
    # 중력 적용
    # -1 여부까지 같이 고려할 수 있는 형태여야되
    # -1 보고나서는 다른 구간으로 인식하는 것으로 여러번
    for c in range(N):
        stop_idx = []

        # -1이 되는 곳 구간을 기준으로 설정해야됨
        # 순서대로 탐색하고 밑에 쌓인 것을 pop으로 뽑도록
        # 구간 나눌 수 잇게 인덱스부터 수집
        start_idx = 0
        start_flag = False
        for r in range(N):
            if block_map[r][c] == -1:
                if r == 0:
                    continue
                stop_idx.append(r)
            elif block_map[r][c] != -1:
                if not start_flag:
                    start_idx = r
                    start_flag = True

        # 구간 만들기
        moments = []
        for s_idx in stop_idx:
            partial = (start_idx, s_idx - 1)
            moments.append(partial)
            start_idx = s_idx + 1

        # 끝부분 처리, 없는 경우도 대비됨
        if start_idx <= N - 1:
            moments.append((start_idx, N - 1))

        # 작은 구간안에서 중력 적용
        print(moments)
        for start_y, end_y in moments:
            stack = []
            for r in range(end_y, start_y - 1, -1):
                if block_map[r][c] != 100 and block_map[r][c] != -1:
                    stack.append(block_map[r][c])

            # 빈공간 채우기
            r_idx = end_y
            for add_block in stack:
                block_map[r_idx][c] = add_block
                r_idx -= 1

            # 남은 윗공간은 빈 공간으로 만들기
            for r in range(r_idx, start_y-1, -1):
                block_map[r][c] = 100

        pprint(block_map, width=30)

    return block_map

def solution(N, M, block_map):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    groups = []
    answer = [0]
    end_flag = [False]
    def find_group():
        #pprint(block_map)
        visited = [[False] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if 0 < block_map[r][c] <= M and not visited[r][c]:
                    candidates = []
                    block_idx = block_map[r][c]
                    queue = deque([(r, c)])
                    rainbow_cnt = 0
                    while queue:
                        start_y, start_x = queue.popleft()
                        visited[start_y][start_x] = True
                        if block_map[start_y][start_x] == 0:
                            rainbow_cnt += 1
                        candidates.append((block_map[start_y][start_x], start_y, start_x))

                        for dy, dx in directions:
                            ny, nx = start_y+dy, start_x+dx
                            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] \
                                and (block_map[ny][nx] == 0 or block_map[ny][nx] == block_idx):
                                visited[ny][nx] = True
                                queue.append((ny, nx))

                    # 뽑은 인원이 2개 이상이어야 함
                    #print(candidates)
                    if len(candidates) >= 2:
                        candidates.sort(key=lambda x:(-x[0], x[1], x[2]))
                        _, candi_r, candi_c = candidates[0]
                        groups.append((len(candidates), rainbow_cnt, candi_r, candi_c, candidates))

        if not groups:
            end_flag[0] = True

    def rotate_delete():
        # 정렬
        groups.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
        print(groups[0])
        pprint(block_map, width=30)

        # 정렬 후 삭제 목록으로 삭제하기
        _, _, _, _, delete_blocks = groups[0]
        answer[0] += (len(delete_blocks) ** 2)
        for _, delete_y, delete_x in delete_blocks:
            block_map[delete_y][delete_x] = 100

        # 일반 블록이 없으면 종료
        is_in_block = False
        for r in range(N):
            if is_in_block: break
            for c in range(N):
                if 0 < block_map[r][c] <= M:
                    is_in_block = True
                    break

        if not is_in_block:
            end_flag[0] = True

        # 중력 적용

        print("after gravity")
        gravity_map = gravity(block_map)
        pprint(gravity_map, width=30)

        # 회전
        rotate_map = list(map(list, zip(*[row[::-1] for row in block_map])))

        # 재 중력 적용
        print()
        print("second gravity")
        gravity(rotate_map)
        return rotate_map

    while True:
        print(f"turn")
        pprint(block_map, width=30)
        print("find_group")
        find_group()
        if end_flag[0]:
            break

        print("delete and rotate")
        rotate_map = rotate_delete()
        if end_flag[0]:
            break
        block_map = rotate_map

        # group 초기화
        groups = []
        print(answer[0])
        print()

    #pprint(block_map)
    return answer[0]



if __name__ == "__main__":
    N, M = map(int, input().split())
    block_map = []
    for _ in range(N):
        block_map.append(list(map(int, input().split())))

    print(solution(N, M, block_map))