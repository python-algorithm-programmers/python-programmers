from collections import deque
import sys
sys.setrecursionlimit(10000)

def dfs(idx, cnt, virus_choice, total_choice):
    if cnt == M:
        total_choice.append(virus_choice[:])
        return

    if idx == N*N:
        return

    dfs(idx+1, cnt, virus_choice, total_choice)
    y, x = idx // N, idx % N
    if maps[y][x] == 2:
        virus_choice.append((y,x))
        dfs(idx+1, cnt+1, virus_choice, total_choice)
        virus_choice.pop()

def solution(N,M,maps):
    virus_choice = []
    total_choice = []
    dfs(0, 0, virus_choice, total_choice)
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    best_turn = []
    for virus_combi in total_choice:
        copy_maps = [row[:] for row in maps]
        for virus_y, virus_x in virus_combi:
            copy_maps[virus_y][virus_x] = 3
        queue = deque(virus_combi)
        visited = [[False]*N for _ in range(N)]
        turn = -1
        while queue:
            for _ in range(len(queue)):
                start_y, start_x = queue.popleft()
                visited[start_y][start_x] = True
                copy_maps[start_y][start_x] = 2
                for dy, dx in directions:
                    ny, nx = start_y+dy, start_x+dx
                    if 0<=ny<N and 0<=nx<N and \
                        not visited[ny][nx] and (copy_maps[ny][nx] == 0 or copy_maps[ny][nx] == 2):
                        queue.append((ny,nx))

                        # 다른 탐색에 중복 방지
                        copy_maps[ny][nx] = 2
                        visited[ny][nx] = True

            turn += 1
        if 1 in [1 for row in copy_maps if 0 in row]:
            pass
        else:
            best_turn.append(turn)
    best_turn.sort()
    return best_turn[0] if best_turn else -1


if __name__ == "__main__":
    N,M = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    print(solution(N,M,maps))