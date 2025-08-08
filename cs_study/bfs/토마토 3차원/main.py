from collections import deque


def bfs(M, N, tomato_maps, directions, visited):
    queue = deque()
    for r in range(N):
        for c in range(M):
            if not visited[r][c] and tomato_maps[r][c] == 1:
                queue.append((r, c))
                visited[r][c] = True

    turn_cnt = -1
    while queue:
        for _ in range(len(queue)):
            y, x = queue.popleft()
            for dy, dx in directions:
                ny, nx = y+dy, x+dx

                if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and tomato_maps[ny][nx]==0:
                    visited[ny][nx] = True
                    tomato_maps[ny][nx] = 1
                    queue.append((ny, nx))

        turn_cnt += 1
    return turn_cnt


def solution(M, N, tomato_maps):
    directions = [(0,-1),(0,1),(-1,0),(1,0)]
    visited = [[False]*M for _ in range(N)]

    cnt = bfs(M, N, tomato_maps, directions, visited)

    # 만약에 bfs 돌고 남았다면, -1
    for row in tomato_maps:
        if 0 in row:
            return -1

    return cnt

if __name__ == "__main__":
    M, N = map(int, input().split())
    tomato_maps = []
    for _ in range(N):
        tomato_maps.append(list(map(int, input().split())))

    print(solution(M, N, tomato_maps))