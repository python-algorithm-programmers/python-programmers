"""
1, 2, 3, 4 -> 위, 아래, 오른쪽, 왼쪽
s -> 속력
d -> 이동 방향
z -> 크기
"""

def solution(R, C, shark_info):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    maps = [[[] for _ in range(C)] for _ in range(R)]
    answer = 0
    shark_where = []

    # 상어 배치 및 상어 위치 기록
    for r, c, s, d, z in shark_info:
        maps[r][c] = [(s, d, z)]
        shark_where.append((r, c))

    # column 크기만큼만 탐색
    for j in range(C):
        # 상어 잡기
        for i in range(R):
            if maps[i][j]:
                s, d, z = maps[i][j][0]
                answer += z

                if (i, j) in shark_where:
                    shark_where.remove((i, j))
                break


        # 상어 위치 찾고 상어 이동시키기
        new_maps = [[[] for _ in range(C)] for _ in range(R)]
        new_share_where = []
        for r, c in shark_where:
            s, d, z = maps[r][c][0]

            # 위/아래
            # 주기가 왕복으로 갓다와서 2배
            if d in (0, 1):
                cycle = (R - 1) * 2
                s %= cycle

            else:
                cycle = (C - 1) * 2
                s %= cycle

            y, x = r, c
            # 1초에 한칸 이동
            for _ in range(s):
                dy, dx = directions[d]
                ny, nx = dy+y, dx+x

                # 담장 넘어가면 위에꺼 그대로 쓰지 않고 바꿔서 만들어라
                if ny < 0 or ny >= R or nx < 0 or nx >= C:
                    if d == 0: d = 1
                    elif d == 1: d = 0
                    elif d == 2: d = 3
                    else: d = 2

                    dy, dx = directions[d]
                    ny, nx = dy+y, dx+x

                y, x = ny, nx

            new_maps[y][x].append((s, d, z))
            new_share_where.append((y, x))

        # 같은 위치에 있는 상어가 있다면 큰 놈이 차지
        final_where = set()
        for r, c in new_share_where:
            if len(new_maps[r][c]) >= 2:
                new_maps[r][c].sort(key=lambda x:-x[2])
                max_shark = new_maps[r][c][0]
                new_maps[r][c] = [max_shark]
            final_where.add((r, c))


        # 새로 바뀐 맵으로 리뉴얼
        maps = new_maps
        shark_where = list(final_where)

    return answer

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    R, C, M = map(int, input().split())
    shark_info = []
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        shark_info.append((r-1, c-1, s, d-1, z))
    print(solution(R, C, shark_info))