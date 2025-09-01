from collections import deque


def solution(N, L, R, maps):
    turn = 0
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    while True:
        near_ctr_list = []
        near_sum_list = []
        visited = [[False] * N for _ in range(N)]
        # 전구간의 visited가 true가 된 경우, 종료
        for y in range(N):
            for x in range(N):
                # 방문안한 곳이 있다면, 이 지역은 여전히 탐색
                if not visited[y][x]:
                    end_flag = False

                queue = deque()
                queue.append((y,x))
                queue_turn_list = [(y,x)]
                sum_turn = maps[y][x]
                while queue:
                    start_y, start_x = queue.popleft()
                    visited[start_y][start_x] = True
                    for dy, dx in directions:
                        ny, nx = start_y+dy, start_x+dx
                        if 0<=ny<N and 0<=nx<N and not visited[ny][nx]\
                            and L<=abs(maps[ny][nx]-maps[start_y][start_x])<=R:
                            visited[ny][nx] = True
                            queue_turn_list.append((ny,nx))
                            queue.append((ny,nx))
                            sum_turn += maps[ny][nx]

                if len(queue_turn_list) > 1:
                    near_ctr_list.append(queue_turn_list)
                    near_sum_list.append(sum_turn)

        # 인접한 나라가 없는 경우
        if not near_ctr_list:
            return turn

        # 평균값으로 맵핑
        for near_ctrs, near_sum in zip(near_ctr_list, near_sum_list):
            for y, x in near_ctrs:
                maps[y][x] = near_sum // len(near_ctrs)

        turn += 1


if __name__ == "__main__":
    N, L, R = map(int, input().strip().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().strip().split())))
    print(solution(N, L, R, maps))