def pprint(arrs):
    for row in arrs:
        print(row)

def get_fall_distance(block_idx, block_map):
    dist = 0
    r, c = block_info[block_idx]["loc"]
    h, w, _ = block_info[block_idx]["first"]


    while True:
        nr = r + 1 + dist

        # 바닥에 닿인 경우
        if nr + h - 1 >= N:
            break

        can_build = True
        for y in range(nr, nr + h):
            if not can_build: break
            for x in range(c, c+w):
                if block_map[y][x] not in [0, block_idx]:
                    can_build = False
                    break

        if not can_build:
            break

        dist += 1
    return dist


def solution(N, M, block_info):
    block_map = [[0]*N for _ in range(N)]
    answer = []

    """ 택배 쌓기 """
    def input_block():
        block_key = list(block_info.keys())
        for block_idx in block_key:
            block_h, block_w, block_c = block_info[block_idx]["first"]

            # 블록 쌓을 수 있는 지 검증하고 위로 쌓아가기
            is_build = False
            for y in range(N-1, -1, -1):
                if is_build: break
                can_build = True
                for r in range(y, y-block_h, -1):
                    if not can_build: break
                    for c in range(block_c, block_c+block_w):
                        if block_map[r][c] != 0:
                            can_build = False
                            break

                if can_build:
                    block_info[block_idx]["loc"] = [y-block_h+1, block_c]
                    for r in range(y, y-block_h, -1):
                        for c in range(block_c, block_c+block_w):
                            block_map[r][c] = block_idx
                    is_build = True

    """좌측 택배 하차"""
    def block_out(flag):
        candidates = set()
        if flag:  # 왼쪽 하차
            visible = []
            for r in range(N):
                for c in range(N):
                    if block_map[r][c] != 0:
                        visible.append(block_map[r][c])
                        break
        else:  # 오른쪽 하차
            visible = []
            for r in range(N):
                for c in range(N - 1, -1, -1):
                    if block_map[r][c] != 0:
                        visible.append(block_map[r][c])
                        break


        # 왼쪽에 있는 것을 떼내기
        if flag:  # 왼쪽
            for block_idx in set(visible):
                by, bx = block_info[block_idx]["loc"]
                h, w, _ = block_info[block_idx]["first"]
                is_block = False
                for y in range(by, by + h):
                    for x in range(0, bx):
                        if block_map[y][x] != 0:
                            is_block = True
                            break
                    if is_block:
                        break
                if not is_block:
                    candidates.add(block_idx)
        else:  # 오른쪽
            for block_idx in set(visible):
                by, bx = block_info[block_idx]["loc"]
                h, w, _ = block_info[block_idx]["first"]
                is_block = False
                for y in range(by, by + h):
                    for x in range(bx + w, N):
                        if block_map[y][x] != 0:
                            is_block = True
                            break
                    if is_block:
                        break
                if not is_block:
                    candidates.add(block_idx)

        # 후보자군 중에서 제일 작은 것 선택하고 빼내기
        candidates = list(candidates)
        candidates.sort()
        candidate_idx = candidates[0]
        answer.append(candidates[0])

        candi_r, candi_c = block_info[candidate_idx]["loc"]
        candi_h, candi_w, _ = block_info[candidate_idx]["first"]

        # 목록에서 제외
        del block_info[candidate_idx]

        # 맵에서 지우기
        for r in range(candi_r, candi_r+candi_h):
            for c in range(candi_c, candi_c+candi_w):
                block_map[r][c] = 0

        # 중력 적용
        """
        빠지는 블록의 최종 x좌표보다 이하일 때
        중간에 근데 막는 블록이 있으면 거기까지 중력적용
        - 구간 적용
        - 무조건 블록 단위로 계산해라
        """
        fall_backs = []
        # 중력 적용 대상 찾기
        for block_idx, info in block_info.items():
            block_r, block_c = info["loc"]
            block_h, block_w, _ = info["first"]

            if block_r + block_h - 1 < candi_r:
                fall_backs.append(block_idx)

        # y가 큰 순으로 해야 맞게 적용됨
        fall_backs.sort(key=lambda x:-block_info[x]["loc"][0])

        # 떨어지는 거리 구하고
        # 그 거리만큼 떨어진 거리만큼 만듦
        for block_idx in fall_backs:
            dist = get_fall_distance(block_idx, block_map)

            # 원래 위치 삭제
            block_r, block_c = block_info[block_idx]["loc"]
            block_h, block_w, _ = block_info[block_idx]["first"]
            for y in range(block_r, block_r+block_h):
                for x in range(block_c, block_c+block_w):
                    block_map[y][x] = 0

            # 바꾼 위치로 집어넣기
            new_r = block_r + dist
            for y in range(new_r, new_r+block_h):
                for x in range(block_c, block_c+block_w):
                    block_map[y][x] = block_idx

            # 바뀐 위치 반영
            block_info[block_idx]["loc"] = [new_r, block_c]

    input_block()
    idx = 1
    #pprint(block_map)
    while True:
        #print(f"{idx} turn")
        block_out(True)
        #print("block out left")
        #print(block_info)
        #pprint(block_map)
        if not block_info:
            break


        block_out(False)
        #print("block out right")
        #print(block_info)
        #pprint(block_map)
        if not block_info:
            break
        idx += 1
        #print()

    return answer




if __name__ == "__main__":
    N, M = map(int, input().split())
    block_info = {}
    for _ in range(M):
        k, h, w, c = map(int, input().split())
        loc = {}
        loc["first"] = [h, w, c-1]
        loc["loc"] = []
        block_info[k] = loc

    ans = solution(N, M, block_info)
    for i in ans:
        print(i)