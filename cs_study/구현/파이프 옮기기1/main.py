def solution(N, maps):
    pos = {
        0: [0, 1],
        1: [0, 1, 2],
        2: [1, 2]
    }
    real_pos = [(0, 1), (1, 1), (1, 0)]
    total_cnt = [0]

    def dfs(cur_pos, cur_loc):
        # 종점 지점에 정확히 도달해야 성공
        if cur_loc == [N-1, N-1]:
            total_cnt[0] += 1
            return

        # 범위를 넘어간 경우는 탈락
        if cur_loc[0] >= N or cur_loc[1] >= N:
            return

        move_cases = pos[cur_pos]
        cur_y, cur_x = cur_loc[0], cur_loc[1]
        for case in move_cases:
            dy, dx = real_pos[case]
            ny, nx = cur_y + dy, cur_x + dx

            # 범위 넘지 않거나 빈칸인 경우에 한해서만
            if 0 <= ny < N and 0 <= nx < N:
                # 가로나 세로인 경우
                if case in [0, 2]:
                    if maps[ny][nx] == 0:
                        dfs(case, [ny, nx])

                # 대각선인 경우
                else:
                    # 다음 지점의 좌, 상을 모두 고려
                    if maps[ny][nx] == 0 and maps[ny-1][nx] == 0 \
                        and maps[ny][nx-1] == 0:
                        dfs(case, [ny, nx])

    dfs(0, [0, 1])
    return total_cnt[0]

if __name__ == "__main__":
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    print(solution(N, maps))