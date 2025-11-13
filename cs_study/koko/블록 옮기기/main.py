from collections import deque

# 1:오른쪽, 2:아래, 3:왼쪽, 4:위
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solution(board, commands):
    n, m = len(board), len(board[0])

    def get_cells(app_id):
        return [(i, j) for i in range(n) for j in range(m) if board[i][j] == app_id]

    def move(app_id, direction):
        di, dj = dirs[direction - 1]
        visited = set()
        queue = deque([app_id])
        to_move = []

        # 1️⃣ 이동에 영향을 받는 앱들을 모두 큐로 수집 (BFS)
        while queue:
            cur = queue.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            cells = get_cells(cur)
            if not cells:
                continue

            # 이동 후 좌표 계산
            new_positions = []
            for i, j in cells:
                ni, nj = (i + di) % n, (j + dj) % m
                new_positions.append((ni, nj))

            # 이동 후 위치에 다른 앱이 있으면 큐에 추가
            for ni, nj in new_positions:
                nxt = board[ni][nj]
                if nxt != 0 and nxt not in visited:
                    queue.append(nxt)

            to_move.append((cur, cells, new_positions))

        # 2️⃣ 실제 이동 처리 (모두 0으로 초기화 후 다시 채우기)
        for cur, cells, _ in to_move:
            for i, j in cells:
                board[i][j] = 0
        for cur, _, new_positions in to_move:
            for ni, nj in new_positions:
                board[ni][nj] = cur

    for app_id, direction in commands:
        move(app_id, direction)

    return board

board = [
 [0,2,2,0,0,0],
 [4,4,2,0,0,0],
 [0,3,3,1,4,4],
 [0,3,3,1,4,0],
 [0,0,0,5,5,0]
]
commands = [[3,1],[3,1],[3,1]]

print(solution(board, commands))