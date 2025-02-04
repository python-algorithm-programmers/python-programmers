
# 장애물이라 어떻게 판단할 것인가?
# 갔던 곳은 read 완료, 상하좌우 가기, 배열 밖으로 나가진 않기
from collections import deque
def bfs(N, maps, visited, start_y, start_x):
    # 상, 하, 좌, 우 순으로 시계 방향으로 방향 결정
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # 시작 지점
    visited[start_y][start_x] = True

    # BFS 위해 큐 초기화 및 시작 위치 (0, 0) + 누적 블록 수를 출력(장애 블럭 수)
    cnt = 1 # 시작 위치 블록 포함
    queue = deque([(start_y, start_x)])

    # 큐가 없을 때까지 반복
    while queue:
        # 큐에서 제거해가면서 탐색
        y, x = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]

            # 범위 내이고, 방문하지 않고, 장애물이 있는 경우
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx] and maps[ny][nx] == 1:
                visited[ny][nx] = True
                cnt += 1
                queue.append((ny, nx))

    return cnt

def solution(N, maps):
    # 방문 처리 위한 2차원 리스트
    visited = [[False] * N for __ in range(N)]

    # 각 블록 크기 저장 리스트
    block_size = []

    # 블록 찾기 (1 찾기)
    for y in range(N):
        for x in range(N):
            if maps[y][x] == 1 and not visited[y][x]:
                cnt = bfs(N, maps, visited, y, x)
                block_size.append(cnt)


    print(len(block_size))
    block_size.sort()
    for block in block_size:
        print(block)

if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline().strip())

    # 맵 결정
    lines = sys.stdin.readlines()
    maps = [list(map(int, line.strip())) for line in lines]
    # N = 7
    # maps = [['1110111'], ['0110101'], ['0110101'], ['0000100'], ['0110000'], ['0111110'], ['0110000']]
    solution(N, maps)


