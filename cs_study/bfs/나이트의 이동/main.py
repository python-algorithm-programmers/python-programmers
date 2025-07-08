from collections import deque


def bfs(N, start_pt, end_pt, maps, visited):
    start_y, start_x = start_pt[1], start_pt[0]
    queue = deque([(start_y, start_x)])
    directions = [
        (sy * dy, sx * dx)
        for dy, dx in ((1,2), (2,1))
        for sx in (1, -1)
        for sy in (1, -1)
    ]

    visited[start_y][start_x] = True
    end_y, end_x = end_pt[1], end_pt[0]
    cnt = 0

    while queue:
        # 현재 큐 크기만큼 확산할 노드들
        for _ in range(len(queue)):
            y, x = queue.popleft()
            if y == end_y and x == end_x:
                return cnt

            for dy, dx in directions:
                ny, nx = y+dy, x+dx
                if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))

        cnt += 1

    # 도달 불가할 시
    return -1
def solution(tests):
    results = []
    for N, start_pt, end_pt, maps, visited in tests:
        result = bfs(N, start_pt, end_pt, maps, visited)
        results.append(result)

    return results

if __name__ == "__main__":
    import sys
    test_cnt = int(sys.stdin.readline())
    tests = []
    for __ in range(test_cnt):
        N = int(sys.stdin.readline())
        start_pt = list(map(int, sys.stdin.readline().split(" ")))
        end_pt = list(map(int, sys.stdin.readline().split(" ")))
        maps = [[0]*N for _ in range(N)]
        # 목표 지점을 1로 지정
        maps[end_pt[1]][end_pt[0]] = 1
        visited = [[False]*N for _ in range(N)]
        tests.append((N, start_pt, end_pt, maps, visited))
    print(solution(tests))