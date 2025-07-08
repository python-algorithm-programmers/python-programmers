from collections import deque

def bfs(y, x, maps, visited, M, N):
    # 다녀간 곳은 방문 등록
    visited[y][x] = True
    queue = deque([(y,x)])
    area = 1
    while queue:
        start_y, start_x = queue.popleft()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for dy, dx in directions:
            ny, nx = start_y+dy, start_x+dx
            if 0<=ny<M and 0<=nx<N and not visited[ny][nx] \
                and maps[ny][nx] == 0:
                    area += 1
                    queue.append((ny,nx))
                    visited[ny][nx] = True

    return area

def solution(M, N, maps):
    areas = []
    visited = [[False]*N for __ in range(M)]
    for y in range(M):
        for x in range(N):
            if not visited[y][x] and maps[y][x] == 0:
                area = bfs(y, x, maps, visited, M, N)
                areas.append(area)
    return areas

if __name__ == "__main__":
    import sys
    M, N, K = list(map(int, sys.stdin.readline().split(" ")))
    lines = sys.stdin.readlines()
    maps = [[0]*N for __ in range(M)]
    for line in lines:
        x1, y1, x2, y2 = list(map(int, line.split(" ")))
        for out_y in range(y1,y2):
            for out_x in range(x1,x2):
                maps[out_y][out_x] = 1

    result = solution(M, N, maps)
    result.sort()
    print(len(result))
    print(result)
