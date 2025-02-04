def dfs(cell_idx, best, pair, current_sum, visited, N, maps):
    # 종료 조건,
    if pair == 4 or cell_idx == N*N:
        best[0] = max(best[0], current_sum)
        return

    # 현재 위치 지정
    y = cell_idx // N
    x = cell_idx % N

    # 현재 위치 확인
    if visited[y][x]:
        dfs(cell_idx+1, best, pair, current_sum, visited, N, maps)
    else:
        # 선택을 안하고 다음것으로 넘어갈 수도 있음
        dfs(cell_idx + 1, best, pair, current_sum, visited, N, maps)

        # 4방향 분석 (상,하,좌,우)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for dy, dx in directions:
            ny = y+dy
            nx = x+dx

            # 범위 확인, 조건을 만족 못시키면 return 되어 이전 것으로 돌아간다
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                # 현재 위치 방문으로 지정
                visited[y][x] = True

                # 옮긴 위치도 방문 지정 + 합계합산
                sum = maps[y][x] + maps[ny][nx]
                visited[ny][nx] = True

                # 다음칸으로 이동
                dfs(cell_idx+1, best, pair+1, current_sum+sum, visited, N, maps)

                # return된 거 다시 순환돌 수 있도록 pair 쌍 부분들 해제
                visited[ny][nx] = False
                visited[y][x] = False

def solution(N, maps):
    # 방문 위치 확인
    visited = [[False]*N for __ in range(N)]

    # 최고값을 list로 설정해서 참조할 수 있도록 설정
    best = [0]

    dfs(0, best, 0, 0, visited, N, maps)
    return best[0]


if __name__ == "__main__":
    import sys
    # N = int(sys.stdin.readline().strip())
    #
    # # map 구현
    # lines = sys.stdin.readlines()
    # maps = [list(map(int, line.split(" "))) for line in lines]
    N = 4
    maps = [[2, 1, 3, 3], [5, 1, 2, 1], [2, 1, 2, 3], [5, 1, 1, 1]]
    print(solution(N, maps))