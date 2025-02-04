from collections import deque
from sys import stdin
from datetime import datetime, timedelta


def bfs(N, maps, visited, start_y, start_x):
    """
    BFS를 활용하여 시작 좌표 (start_y, start_x)에서 연결된 장애물(1) 블록의 크기를 반환
    """
    # 상, 하, 좌, 우 방향 (행, 열 기준)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    queue = deque([(start_y, start_x)])
    visited[start_y][start_x] = True
    cnt = 1  # 시작 위치 포함

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            # 범위 내이고, 아직 방문하지 않았으며, 장애물(1)인 경우
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and maps[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((ny, nx))
                cnt += 1
    return cnt


def solution(N, maps):
    # 방문 여부를 체크할 2차원 리스트
    visited = [[False] * N for _ in range(N)]

    block_sizes = []  # 각 블록 내 장애물 수 저장
    # 전체 블록(연결된 1들의 그룹)을 찾기 위해 전체 셀을 순회
    for y in range(N):
        for x in range(N):
            if maps[y][x] == 1 and not visited[y][x]:
                size = bfs(N, maps, visited, y, x)
                block_sizes.append(size)

    # 총 블록 수 출력
    print(len(block_sizes))
    # 각 블록 내 장애물 수를 오름차순으로 정렬하여 출력
    for size in sorted(block_sizes):
        print(size)


if __name__ == "__main__":
    import sys

    # 첫 줄: N (격자의 크기)
    N = int(sys.stdin.readline().strip())

    # 그 다음 N줄: 격자 정보 (각 줄에 공백 없이 0 또는 1들이 주어짐)
    # 예) "1110111" → [1,1,1,0,1,1,1]
    maps = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

    solution(N, maps)