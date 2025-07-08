from collections import deque
def bfs(M, N, maps, visited):
    queue = deque()
    # 시작점이 여러개라서 bfs 로직에서 큐를 넣을 때 여러 개를 넣음
    for row in range(N):
        for col in range(M):
            if maps[row][col] == 1:
                queue.append((row, col))
                visited[row][col] = True

    # 상하좌우, 튜플 리스트
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    # 처음 시작점 도착이 0일로 되기 위해
    days = -1
    while queue:
        # 맨처음 시작점 도착
        days += 1

        # 오늘 익을 토마토 수만큼만 처리
        # 하루가 지날 때 그날 익은 토마토 모두 처리해야됨
        # 익은 토마토가 전방위적으로 처리되도록
        for _ in range(len(queue)):
            y, x = queue.popleft()
            for dy, dx in directions:
                ny, nx = y+dy, x+dx
                # 범위 안 넘으면서, 익음처리 안당한 싱싱한 토마토
                if 0<=ny<N and 0<=nx<M and not visited[ny][nx] \
                   and maps[ny][nx]==0:
                    # 익음 처리
                    maps[ny][nx] = 1
                    visited[ny][nx] = True
                    queue.append((ny,nx))
    return days

def solution(M, N, maps):
    # 익음 처리
    visited = [[False]*M for __ in range(N)]

    # 시작점이 여러개가 될 수 있으므로 온전히 bfs내에서 시작점을 모두 찾아서 큐에넣고
    # 큐가 있는 상황을 전제로 나아갈 때마다 하나씩 추가하고, 없으면 큐가 안쌓이는 형태
    days = bfs(M, N, maps, visited)

    # bfs 돌았는 데 아직 남으면 -1 반환
    for row in maps:
        if 0 in row:
            return -1
    return days

if __name__ == "__main__":
    import sys
    M, N = list(map(int, sys.stdin.readline().split(" ")))
    lines = sys.stdin.readlines()
    maps = []
    for line in lines:
        maps.append(list(map(int, line.split(" "))))
    print(solution(M, N, maps))