from collections import deque
def dfs(idx, check_cnt, sum_beauty, best, N, visited, maps):
    y, x = idx // N, idx % N
    # 종료조건
    # 4개를 골랐을 때 or 끝까지 도달했을 때
    if check_cnt == 4 or idx == N*N:
        best[0] = max(best[0], sum_beauty)
        return

    # 현재 셀이 이미 사용됬는 지 여부 확인
    if visited[y][x]:
        dfs(idx + 1, check_cnt, sum_beauty, best, N, visited, maps)

    else:
        # 그냥 넘어가기
        dfs(idx+1, check_cnt, sum_beauty, best, N, visited, maps)

        # 4방향 bfs 시작
        queue = deque([(y,x)])
        directions = [(-1,0), (0,1), (1,0), (0,-1)]

        while queue:
            cur_y, cur_x = queue.popleft()
            for dy, dx in directions:
                ny, nx = cur_y+dy, cur_x+dx

                if (0<=ny<N and 0<=nx<N and not visited[ny][nx]):
                    # 선택
                    visited[cur_y][cur_x] = True
                    visited[ny][nx] = True

                    # 합산
                    pair_sum = maps[cur_y][cur_x] + maps[ny][nx]

                    # 다음으로 넘어가기
                    dfs(idx+1, check_cnt+1, sum_beauty+pair_sum, best, N, visited, maps)

                    # 복귀하고 온 탕아에 대해선 다음 for문 적용해야되므로 초기화
                    visited[cur_y][cur_x] = False
                    visited[ny][nx] = False


def solution(N, maps):
    visited = [[False]*N for __ in range(N)]
    best = [0]

    dfs(0, 0, 0, best, N, visited, maps)
    return best[0]

if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline().strip())
    maps = []
    for __ in range(N):
        maps.append(list(map(int, sys.stdin.readline().strip().split(" "))))

    print(solution(N, maps))