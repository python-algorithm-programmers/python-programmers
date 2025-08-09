import copy
from collections import deque

def bfs(points, N, M, maps):
    maps_one = [row[:] for row in maps]

    # 벽 추가
    for point in points:
        add_y, add_x = point
        maps_one[add_y][add_x] = 1

    # 바이러스 확장 시작
    # 시작점 파악
    virus_start_p = []
    for i in range(N):
        for j in range(M):
            if maps_one[i][j] == 2:
                virus_start_p.append((i,j))

    # 시작점을 큐에 모두 넣어서 확장시작
    queue = deque(virus_start_p)
    visited = [[False]*M for _ in range(N)]
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    while queue:
        start_y, start_x = queue.popleft()
        visited[start_y][start_x] = True
        maps_one[start_y][start_x] = 2
        for dy, dx in directions:
            ny, nx = start_y+dy, start_x+dx
            if 0<=ny<N and 0<=nx<M and maps_one[ny][nx]==0 and not visited[ny][nx]:
                queue.append((ny, nx))

    answer = 0
    # 0인 곳만 색출
    for r in range(N):
        for c in range(M):
            if maps_one[r][c] == 0:
                answer += 1

    return answer

def dfs(idx, points, best, maps, N, M):
    if len(points) == 3:
        able_cnt = bfs(points, N, M, maps)
        best[0] = max(best[0], able_cnt)
        return

    if idx == N*M:
        return

    dfs(idx+1, points, best, maps, N, M)
    cur_y, cur_x = idx // M, idx % M

    # 빈칸이면 벽으로 만들기
    if maps[cur_y][cur_x] == 0:
        points.append((cur_y, cur_x))
        dfs(idx+1, points, best, maps, N, M)
        points.pop()

def solution(N,M,maps):
    points = []
    best = [0]
    dfs(0, points, best, maps, N, M)
    return best[0]

if __name__ == "__main__":
    N, M = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    print(solution(N,M,maps))