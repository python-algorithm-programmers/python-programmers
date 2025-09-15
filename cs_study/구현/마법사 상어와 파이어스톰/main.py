from collections import deque


def rotate(arr):
    return [list(arr) for arr in zip(*arr[::-1])]

def solution(N, maps, square_list):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    size = 2**N

    # 격자구조로 회전
    for L in square_list:
        block = 2 ** L
        for y in range(0, size, block):
            for x in range(0, size, block):
                small_map = []
                for r in range(y, y+block):
                    small_line = []
                    for c in range(x, x+block):
                        small_line.append(maps[r][c])
                    small_map.append(small_line)

                # map 회전
                small_map = rotate(small_map)

                # 회전한 map을 다신 처음 위치에 둔다
                for r in range(y, y+block):
                    for c in range(x, x+block):
                        maps[r][c] = small_map[r-y][c-x]

        # 주위에 얼음 여부 확인하고 녹이기
        # 동시에 접근하기 위해 ice_map 적용
        ice_maps = [row[:] for row in maps]
        for i in range(size):
            for j in range(size):
                if ice_maps[i][j] == 0: continue
                ice_cnt = 0
                for dy, dx in directions:
                    ny, nx = i+dy, j+dx
                    if 0<= ny < size and 0 <= nx < size and ice_maps[ny][nx] > 0:
                        ice_cnt += 1

                # 3 미만이면 그 칸은 -1
                if ice_cnt < 3:
                    maps[i][j] -= 1

    # 얼음의 양을 확인
    total_ice = sum(sum(row) for row in maps)

    # 연결된 얼음의 양을 확인
    visited = [[False]*(size) for _ in range(size)]
    max_cnt = 0

    for y in range(size):
        for x in range(size):
            if not visited[y][x] and maps[y][x]:
                queue = deque()
                queue.append((y, x))
                queue_cnt = 1
                while queue:
                    start_y, start_x = queue.popleft()
                    visited[start_y][start_x] = True
                    for dy, dx in directions:
                        ny, nx = start_y+dy, start_x+dx
                        if (0 <= ny < size and 0 <= nx < size and
                                not visited[ny][nx] and maps[ny][nx] > 0):
                            queue.append((ny,nx))
                            queue_cnt += 1
                            visited[ny][nx] = True

                max_cnt = max(max_cnt, queue_cnt)

    print(total_ice)
    print(max_cnt)


if __name__ == "__main__":
    N, Q = map(int, input().split())
    maps = []
    for _ in range(2**N):
        maps.append(list(map(int, input().split())))

    square_list = []
    for _ in range(1):
        square_list.extend(list(map(int, input().split())))
    solution(N, maps, square_list)