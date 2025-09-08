def solution(N,water_magic,maps):
    directions = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
    expand = [(-1,-1),(-1,1),(1,1),(1,-1)]

    # 첫 구름 생성
    cloud_maps = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if (i == N-2 or i==N-1) and (j==0 or j==1):
                cloud_maps[i][j] = 1

    answer = 0
    for direct_num, distance in water_magic:
        visited = [[False] * N for _ in range(N)]
        dy, dx = directions[direct_num-1]
        ny, nx = dy*distance, dx*distance

        # 구름 이동
        cloud_moves = set()
        for i in range(N):
            for j in range(N):
                if cloud_maps[i][j] == 1:
                    real_y, real_x = i+ny, j+nx
                    # 범위 넘어간 경우나 음수인 경우
                    if i+ny >= N or i+ny < 0:
                        real_y = (i + ny) % N
                    if j+nx >= N or j+nx < 0:
                        real_x = (j + nx) % N

                    # 이동한 자리 물 채우고 구름 삭제
                    cloud_maps[i][j] = 0
                    maps[real_y][real_x] += 1
                    visited[real_y][real_x] = True
                    cloud_moves.add((real_y, real_x))

        # 마법쓰기
        for y, x in cloud_moves:
            move_cnt = 0
            for dy, dx in expand:
                my, mx = y+dy, x+dx
                if 0 <= my < N and 0 <= mx < N and maps[my][mx] >= 1:
                    move_cnt += 1
            maps[y][x] += move_cnt

        # 구름 생성
        for y in range(N):
            for x in range(N):
                if maps[y][x] >= 2 and not visited[y][x]:
                    cloud_maps[y][x] = 1
                    maps[y][x] -= 2

    # 합계 계산
    for i in range(N):
        answer += sum(maps[i])

    return answer

if __name__ == "__main__":
    N, M = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))

    water_magic = []
    for _ in range(M):
        water_magic.append(list(map(int, input().split())))
    print(solution(N,water_magic,maps))