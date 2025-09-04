def dfs(idx, choice_cnt, choices, total_choices, maps):
    if choice_cnt == 3:
        total_choices.append(choices[:])
        return

    if idx == N*M:
        return

    dfs(idx+1, choice_cnt, choices, total_choices, maps)

    y, x = idx // M, idx % M
    if maps[y][x] == 0:
        choices.append((y,x))
        dfs(idx+1, choice_cnt+1, choices, total_choices, maps)
        choices.pop()

def solution(N,M,maps):
    total_choices = []
    choices = []
    dfs_visited = [[False]*M for _ in range(N)]
    dfs(0, 0, choices, total_choices, maps)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    best_cnt = []
    for brick_choice in total_choices:
        copy_maps = [row[:] for row in maps]
        for brick_sel in brick_choice:
            brick_y, brick_x = brick_sel
            copy_maps[brick_y][brick_x] = 1

        visited = [[False]*M for _ in range(N)]
        # 시작점 찾기
        points = []
        for y in range(N):
            for x in range(M):
                if copy_maps[y][x] == 2:
                    points.append((y,x))

        queue = deque(points)
        while queue:
            start_y, start_x = queue.popleft()
            visited[start_y][start_x] = True
            copy_maps[start_y][start_x] = 2

            for dy, dx in directions:
                ny, nx = start_y+dy, start_x+dx

                if 0<=ny<N and 0<=nx<M and copy_maps[ny][nx] == 0 and not visited[ny][nx]:
                    queue.append((ny,nx))

        choice_hall_cnt = sum([1 for y in range(N) for x in range(M) if copy_maps[y][x] == 0])
        best_cnt.append(choice_hall_cnt)

    best_cnt.sort()
    return best_cnt[-1]

if __name__ == "__main__":
    from collections import deque
    N,M = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    print(solution(N,M,maps))