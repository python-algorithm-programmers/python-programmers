from collections import deque

def bfs(N, M, maps, break_visited):
    queue = deque()
    queue.append((0,0))
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    while queue:
        start_y, start_x = queue.popleft()
        current_best_breaks = break_visited[start_y][start_x]

        if start_y == N - 1 and start_x == M - 1:
            break

        for dy, dx in directions:
            ny, nx = start_y+dy, start_x+dx
            if 0<=ny<N and 0<=nx<M:
                brick = maps[ny][nx]

                # 최선인 것만 탐색
                if current_best_breaks + brick < break_visited[ny][nx]:
                    break_visited[ny][nx] = current_best_breaks + brick

                    if brick == 0:
                        queue.appendleft((ny, nx))
                    else:
                        queue.append((ny, nx))


def solution(maps, N, M):
    best_break = N+M
    break_visited = [[best_break]*M for __ in range(N)]
    break_visited[0][0] = 0
    bfs(N, M, maps, break_visited)
    return break_visited[N-1][M-1]


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