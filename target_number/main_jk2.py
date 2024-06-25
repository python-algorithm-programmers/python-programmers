from collections import deque

def bfs (maps):
    # 초기 세팅
    n, m = len(maps), len(maps[0])

    # 방문 위치를 파악할 추가 map 설정
    visited = [[False]*m for _ in range(n)]

    # 동, 남, 서, 북 순으로
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    # 방문 위치, count 등록
    queue = deque([(0,0,1)])

    # 큐를 뽑아서 탐색 -> 큐를 등록시키면서 조건 만족하는 경로들 추가
    while queue:
        y, x, count = queue.popleft()

        # 종료 조건
        if x == m-1 and y == n-1:
            return count



        for i in range(len(dx)):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny <= n-1 and 0 <= nx <= m-1 and visited[ny][nx] == False and maps[ny][nx] == 1:
                # 다른 경로로 추가될 수 있는 노드의 중복을 제거하기 위해 등록전 false 처리
                visited[ny][nx] = True
                # 방문 가능한 위치들은 모두 등록시키기
                queue.append((ny,nx,count+1))

    return -1

def solution(maps):
    return bfs(maps)


if __name__ == '__main__':
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
