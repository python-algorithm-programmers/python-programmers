def solution(R,C,T,maps,pointers,conditioners):
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    while T > 0:
        # 확산
        dust_map = [row[:] for row in maps]
        for y in range(R):
            for x in range(C):
                if dust_map[y][x] > 0:
                    cnt = 0
                    div_m = dust_map[y][x] // 5
                    if div_m == 0: continue
                    for dy, dx in directions:
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < R and 0 <= nx < C and dust_map[ny][nx] != -1:
                            cnt += 1
                            maps[ny][nx] += div_m

                    maps[y][x] -= div_m * cnt

        # 바람불기, 이동
        first_y, first_x = conditioners[0]
        last_y, last_x = conditioners[1]

        # # 위쪽 반시계 회전
        # up_map = maps[:first_y+1]
        # print(up_map)
        # counter_cw_up_map = [list(row) for row in zip(*up_map)][::-1]
        #
        # # 아래쪽 반시계 회전
        # down_map = maps[last_y:]
        # cw_up_map = [list(row) for row in zip(*down_map[::-1])]

        # 공기청정기 바람 순환
        # 위쪽 (반시계)
        for y in range(first_y-1, 0, -1):
            maps[y][0] = maps[y-1][0]

        for x in range(C-1):
            maps[0][x] = maps[0][x+1]

        for y in range(first_y):
            maps[y][C-1] = maps[y+1][C-1]

        for x in range(C-1, 1, -1):
            maps[first_y][x] = maps[first_y][x-1]
        maps[first_y][1] = 0

        # 아래쪽 (시계)
        for y in range(last_y+1, R-1):
            maps[y][0] = maps[y+1][0]

        for x in range(C-1):
            maps[R-1][x] = maps[R-1][x+1]

        for y in range(R-1, last_y, -1):
            maps[y][C-1] = maps[y-1][C-1]

        for x in range(C-1, 1, -1):
            maps[last_y][x] = maps[last_y][x-1]
        maps[last_y][1] = 0

        T -= 1

    answer = 0
    for i in range(R):
        for j in range(C):
            if maps[i][j] > 0:
                answer += maps[i][j]
    return answer

if __name__ == "__main__":
    R, C, T = map(int, input().split())
    maps = []
    pointers = []
    conditioners = []
    for i in range(R):
        line = list(map(int, input().split()))
        for j in range(C):
            if line[j] != 0 and line[j] != -1:
                pointers.append((i,j,line[j]))
            elif line[j] == -1:
                conditioners.append((i,j))
        maps.append(line)
    print(solution(R,C,T,maps,pointers,conditioners))
