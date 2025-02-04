def dfs(cell_index, pairs, current_sum, n, maps, visited, best):
    # 만약 최대 4쌍을 선택했거나 모든 셀을 처리했다면
    if cell_index >= n * n or pairs == 4:
        best[0] = max(best[0], current_sum)
        return

    # (y, x) 좌표로 변환 (행 우선 순서)
    y = cell_index // n
    x = cell_index % n

    # 현재 셀이 이미 사용되었다면 다음 셀로 진행
    if visited[y][x]:
        dfs(cell_index + 1, pairs, current_sum, n, maps, visited, best)
    else:
        # **옵션 1:** 현재 셀을 사용하지 않고 넘어가기
        dfs(cell_index + 1, pairs, current_sum, n, maps, visited, best)

        # **옵션 2:** 현재 셀과 인접한 셀과 쌍을 이루기
        # 인접 방향: 상, 하, 좌, 우
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            # 범위 내, 인접 셀이 사용되지 않았는지 확인
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                # 방문 처리 (두 셀 모두)
                visited[y][x] = True
                visited[ny][nx] = True

                # 두 셀의 아름다움 (높이의 합)
                pair_sum = maps[y][x] + maps[ny][nx]

                dfs(cell_index + 1, pairs + 1, current_sum + pair_sum, n, maps, visited, best)

                # 백트래킹: 방문 처리 해제
                visited[y][x] = False
                visited[ny][nx] = False


def solution(n, maps):
    # 방문 배열 초기화
    visited = [[False] * n for _ in range(n)]
    best = [0]  # 최대 아름다움 합을 저장 (리스트를 사용하여 참조 전달)

    dfs(0, 0, 0, n, maps, visited, best)
    return best[0]


if __name__ == "__main__":
    import sys

    input_data = sys.stdin.read().splitlines()
    n = int(input_data[0].strip())
    # n개의 줄에 걸쳐 각 행의 나무 높이 정보를 읽음
    maps = [list(map(int, input_data[i].split())) for i in range(1, n + 1)]
    print(solution(n, maps))