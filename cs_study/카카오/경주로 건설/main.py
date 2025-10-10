"""
[[0, 0, 0, 0, 0],
 [0, 1, 1, 1, 0],
 [0, 0, 1, 0, 0],
 [1, 0, 0, 0, 1],
 [1, 1, 1, 0, 0]]

 3000
"""
"""
BFS
cur_dir = 0, 1, directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
현재 방향 우선, 벽보면 다음 directions 설정
코너링 돌면 = 다른 directions 인덱스로 넘어가면 
모든 경우를 못따질 수 있는 문제 발생, for문으로 전부 탐색해서 큐에 넣어야할 꺼 같음
"""
from collections import deque

def solution(board):
    N = len(board)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    best = float("inf")
    for ch in range(2):
        visited = [[float('inf')] * N for _ in range(N)]
        queue = deque([(0,0,0,ch)])
        while queue:
            y, x, q_cost, dir_idx = queue.popleft()
            # 만약 끝지점에 도달했다면, 다음 큐로 진행
            if y == N-1 and x == N-1:
                best = min(best, visited[N-1][N-1])
                continue

            for i in range(len(directions)):
                dy, dx = directions[i]
                ny, nx = y+dy, x+dx
                if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
                    if i == dir_idx:
                        new_cost = q_cost + 100
                    else:
                        new_cost = q_cost + 600

                    if new_cost <= visited[ny][nx]:
                        visited[ny][nx] = new_cost
                        queue.append((ny, nx, new_cost, i))

    return best

if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 1, 0, 0],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 0, 0]]
    print(solution(board))