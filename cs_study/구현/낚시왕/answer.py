"""
s -> 속력
d -> 이동 방향
z -> 크기
"""
def solution(R, C, shark_map, shark_where):
    # 낚시왕의 캐치
    answer = 0
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for fish_man in range(C):
        for i in range(R):
            if shark_map[i][fish_man]:
                s, d, z = shark_map[i][fish_man][0]
                answer += z
                # 상어 위치 삭제
                shark_where.remove((i, fish_man))
                break

        # 상어 이동
        #print(shark_map)
        new_maps = [[[] for _ in range(C)] for _ in range(R)]
        new_shark_where = set()
        #sorted_list = sorted(list(shark_where), key=lambda x: (x[0], x[1]))
        #print(sorted_list)
        for r, c in shark_where:
            s, d, z = shark_map[r][c][0]
            # 방향, 위 아래 나누기
            if d in (0, 1):
                dy = directions[d][0]
                cycle = (R - 1) * 2
                s %= cycle
                ny = r + dy*s
                ny %= cycle

                if ny >= R:
                    if ny > 0:
                        ny = cycle - ny
                    d = 1 - d

                new_shark_where.add((ny, c))
                new_maps[ny][c].append((s, d, z))

            else:
                dx = directions[d][1]
                cycle = (C - 1) * 2
                s %= cycle
                nx = c + dx * s
                nx %= cycle

                if nx >= C:
                    if nx > 0:
                        nx = cycle - nx
                    d = 5 - d

                new_shark_where.add((r, nx))
                new_maps[r][nx].append((s, d, z))

        # 상어 합치기
        for new_r, new_c in new_shark_where:
            if len(new_maps[new_r][new_c]) > 1:
                new_maps[new_r][new_c].sort(key=lambda x:-x[2])
                new_maps[new_r][new_c] = [new_maps[new_r][new_c][0]]

        # 다음 단계에서 반영할 수 있도록 변경
        #print(new_maps)
        #print(sorted(list(new_shark_where), key=lambda x: (x[0], x[1])))
        #print()
        shark_map = new_maps
        shark_where = new_shark_where

    return answer


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    R, C, M = map(int, input().split())
    shark_where = set()
    shark_map = [[[] for _ in range(C)] for _ in range(R)]

    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        shark_map[r-1][c-1] = [(s, d-1, z)]
        shark_where.add((r-1, c-1))
    print(solution(R, C, shark_map, shark_where))