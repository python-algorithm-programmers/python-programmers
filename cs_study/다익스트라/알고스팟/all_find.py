from collections import deque

def bfs(y, x, N, M, maps, visited):
    queue = deque()
    queue.append((y,x,0))
    directions = [(1,0), (0,1)]
    best_break = 5000
    while queue:
        start_y, start_x, breaks = queue.popleft()
        visited[start_y][start_x] = True
        for dy, dx in directions:
            ny, nx = start_y+dy, start_x+dx
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
                if ny == N-1 and nx == M-1:
                    if breaks < best_break:
                        best_break = breaks
                    continue

                if maps[ny][nx] == 0:
                    queue.append((ny, nx, breaks))
                else:
                    queue.append((ny, nx, breaks+1))

    return best_break

def solution(maps, N, M):
    visited = [[False]*M for __ in range(N)]
    best_breaks = bfs(0,0, N, M, maps, visited)
    return best_breaks

if __name__ == "__main__":
    M, N = map(int, input().split())
    maps = []
    for i in range(N):
        lines = input()
        line_map = []
        for j in range(M):
            line_map.append(int(lines[j]))

        maps.append(line_map)
    print(solution(maps, N, M))