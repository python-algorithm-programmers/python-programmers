from collections import deque


def rotate(arr):
    return [list(arr) for arr in zip(*arr[::-1])]

def solution(N, maps, square_list):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    # 격자구조로 회전
    for L in square_list:
        repeated_flag = True
        for y in range(0, 2**N, 2**L):
            if repeated_flag:
                for x in range(0, 2**N, (2**L)*2):
                    small_map = []
                    for r in range(y, y+2**L):
                        small_line = []
                        for c in range(x, x+2**L):
                            small_line.append(maps[r][c])
                        small_map.append(small_line)

                    # map 회전
                    small_map = rotate(small_map)

                    # 회전한 map을 다신 처음 위치에 둔다
                    for r in range(y, y+2**L):
                        for c in range(x, x+2**L):
                            maps[r][c] = small_map[r-y][c-x]

                repeated_flag = False

            else:
                for x in range(2**L, 2**N, (2**L)*2):
                    small_map = []
                    for r in range(y, y + 2 ** L):
                        small_line = []
                        for c in range(x, x + 2 ** L):
                            small_line.append(maps[r][c])
                        small_map.append(small_line)

                    # map 회전
                    small_map = rotate(small_map)

                    # 회전한 map을 다신 처음 위치에 둔다
                    for r in range(y, y + 2 ** L):
                        for c in range(x, x + 2 ** L):
                            maps[r][c] = small_map[r - y][c - x]

                repeated_flag = True

        # 주위에 얼음 여부 확인하고 녹이기
        # 동시에 접근하기 위해 ice_map 적용
        ice_maps = [row[:] for row in maps]
        for i in range(2**N):
            for j in range(2**N):
                if ice_maps[i][j] == 0: continue
                ice_cnt = 0
                for dy, dx in directions:
                    ny, nx = i+dy, j+dx
                    if 0<= ny < 2**N and 0 <= nx < 2**N and ice_maps[ny][nx] > 0:
                        ice_cnt += 1

                # 3 미만이면 그 칸은 -1
                if ice_cnt < 3:
                    maps[i][j] -= 1

    # 얼음의 양을 확인
    total_ice = 0
    ice_on_point = []
    for i in range(2**N):
        for j in range(2**N):
            if maps[i][j] > 0:
                total_ice += maps[i][j]
                ice_on_point.append((i,j))

    # 연결된 얼음의 양을 확인
    visited = [[False]*(2**N) for _ in range(2**N)]
    queue_cnt_list = []
    queue = deque()
    queue_cnt = 0
    for y, x in ice_on_point:
        if visited[y][x]: continue

        queue.append((y, x))
        queue_cnt += 1
        while queue:
            start_y, start_x = queue.popleft()
            visited[start_y][start_x] = True
            for dy, dx in directions:
                ny, nx = y+dy, x+dx
                if (0 <= ny < 2**N and 0 <= nx < 2**N and
                        not visited[ny][nx] and maps[ny][nx] > 0):
                    queue.append((ny,nx))
                    queue_cnt += 1
                    visited[ny][nx] = True

        queue_cnt_list.append(queue_cnt)

    queue_cnt_list.sort()
    return (total_ice, queue_cnt_list[-1])





if __name__ == "__main__":
    N, Q = map(int, input().split())
    maps = []
    for _ in range(2**N):
        maps.append(list(map(int, input().split())))

    square_list = []
    for _ in range(1):
        square_list.extend(list(map(int, input().split())))
    print(solution(N, maps, square_list))