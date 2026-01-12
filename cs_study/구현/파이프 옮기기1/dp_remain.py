def solution(N, maps):
    pos = {
        0: [0, 1],
        1: [0, 1, 2],
        2: [1, 2]
    }
    real_pos = [(0, 1), (1, 1), (1, 0)]
    # y, x, pos로 각 좌표당 3개의 position으로 구분
    dp = [[[-1] * 3 for _ in range(N)] for _ in range(N)]
    def dfs(cur_pos, cur_loc):
        cur_y, cur_x = cur_loc
        if cur_y == N-1 and cur_x == N-1:
            return 1

        # 더 탐색 안하고 캐싱
        if dp[cur_y][cur_x][cur_pos] != -1:
            return dp[cur_y][cur_x][cur_pos]

        cnt = 0
        for case in pos[cur_pos]:
            dy, dx = real_pos[case]
            ny, nx = cur_y+dy, cur_x+dx

            if 0 <= ny < N and 0 <= nx < N:
                if case in [0, 2]:
                    if maps[ny][nx] == 0:
                        cnt += dfs(case, [ny, nx])
                else:
                    if maps[ny][nx] == 0 and maps[ny-1][nx] == 0 \
                        and maps[ny][nx-1] == 0:
                        cnt += dfs(case, [ny, nx])

        # 현재 위치까지 재귀탐색후 얼만큼 경우가 있는 지 지정
        dp[cur_y][cur_x][cur_pos] = cnt
        return cnt

    return dfs(0, [0, 1])





if __name__ == "__main__":
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    print(solution(N, maps))