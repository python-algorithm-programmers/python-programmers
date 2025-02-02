from collections import deque


def bfs_attack(n, m, map_list, l, r):
    """
    BFS를 활용한 나무 공격 수행
    """
    # 이동 방향 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([(l, r)])
    map_list[l][r] = 0  # 나무 쓰러뜨리기

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 유효한 좌표인지 확인
            if 0 <= nx < n and 0 <= ny < m:
                if map_list[nx][ny] > 0:  # 나무가 살아있다면
                    map_list[nx][ny] = 0  # 쓰러뜨리기
                    queue.append((nx, ny))  # 큐에 추가하여 연쇄 공격


def count_remaining_trees(map_list):
    """
    남아 있는 나무의 개수를 계산하는 함수
    """
    return sum(sum(row) > 0 for row in map_list)


def solution(n, m, map_list, l1, r1, l2, r2):
    # 1차 공격 수행
    bfs_attack(n, m, map_list, l1, r1)

    # 2차 공격 수행
    bfs_attack(n, m, map_list, l2, r2)

    # 남아 있는 나무 개수 계산
    return count_remaining_trees(map_list)


if __name__ == "__main__":
    import sys

    sys.stdin = open("input.txt")

    # 입력값 처리
    n, m = map(int, input().split(""))

    # 행렬 입력 받기
    map_list = []
    for _ in range(n):
        lines = list(map(int, input().split()))
        map_list.append(lines)

    # 공격 위치 입력 받기
    l1, r1 = map(int, input().split())
    l2, r2 = map(int, input().split())

    # 결과 출력
    print(solution(n, m, map_list, l1, r1, l2, r2))