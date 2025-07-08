from collections import deque


def bfs(start_y, start_x, M, N, maps, visited):
    area = 1
    visited[start_y][start_x] = True
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    queue = deque([(start_y, start_x)])

    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y+dy, x+dx

            if 0<=ny<M and 0<=nx<N and not visited[ny][nx] \
                and maps[ny][nx]==1:
                visited[ny][nx] = True
                area += 1
                queue.append((ny,nx))

    return area
def solution(M, N, maps):
    results = []
    visited = [[False]*N for _ in range(M)]
    for y in range(M):
        for x in range(N):
            if maps[y][x] == 1 and not visited[y][x]:
                result = bfs(y, x, M, N, maps, visited)
                results.append(result)

    return results


if __name__ == "__main__":
    import sys
    M, N = list(map(int, sys.stdin.readline().split(" ")))
    maps = []
    lines = sys.stdin.readlines()
    for line in lines:
        maps.append(list(map(int, line.split(" "))))

    areas = solution(M, N, maps)
    if not areas:
        print(0)
        print(0)
    else:
        print(len(areas))
        print(max(areas))
