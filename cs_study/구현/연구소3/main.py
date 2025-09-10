def dfs(idx, cnt, choices, total_choices):
    if cnt == M:
        total_choices.append(choices[:])
        return

    if idx == N*N:
        return

    dfs(idx+1, cnt, choices, total_choices)
    y, x = idx // N, idx % N
    if maps[y][x] == 2:
        choices.append((y,x))
        dfs(idx+1, cnt+1, choices, total_choices)
        choices.pop()

def solution(N,M,maps):
    total_choices = []
    choices = []
    dfs(0, 0, choices, total_choices)

    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    best_turn = []
    for choice_sel in total_choices:
        copy_maps = [row[:] for row in maps]
        for virus_y, virus_x in choice_sel:
            copy_maps[virus_y][virus_x] = 3

        visited = [[False] * N for _ in range(N)]
        queue = deque(choice_sel)
        turn = 0
        while queue:
            for _ in range(len(queue)):
                start_y, start_x = queue.popleft()
                visited[start_y][start_x] = True
                for dy,dx in directions:
                    ny,nx = start_y+dy, start_x+dx
                    if 0<=ny<N and 0<=nx<N and not visited[ny][nx] \
                        and copy_maps[ny][nx] != 1:
                        queue.append((ny,nx))
                        visited[ny][nx] = True
                        if copy_maps[ny][nx] == 0:
                            copy_maps[ny][nx] = 3

                    # 비활성화된 바이러스 주위로 그 바이러스만 갈 수 있는 통로가 있다면
                    # 굳이 활성화 시킬 필요없는 비활성 바이러스위에 바이러스 감염시켜서 건너감
                    # elif 0<=ny<N and 0<=nx<N and not visited[ny][nx] \
                    #     and copy_maps[ny][nx] == 2:
                    #     queue.append((ny,nx))
                    #     visited[ny][nx] = True
                    #     copy_maps[ny][nx] = 3

            if queue:
                turn += 1

        if 1 in [1 for row in copy_maps if 0 in row]:
            pass
        else:
            best_turn.append(turn)

    best_turn.sort()
    return best_turn[0] if best_turn else -1


if __name__ == "__main__":
    from collections import deque
    import sys
    sys.setrecursionlimit(5000)

    N,M = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    print(solution(N,M,maps))