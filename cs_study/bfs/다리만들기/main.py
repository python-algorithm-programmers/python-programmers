def pprint(arrs):
    for arr in arrs:
        print(arr)

def dfs(idx, depth, choice, combi, len_combi, dfs_result, final):
    if depth == choice:
        final.append(dfs_result[:])
        return

    if idx == len_combi:
        return

    dfs(idx+1, depth, choice, combi, len_combi, dfs_result, final)

    dfs_result.append(combi[idx])
    dfs(idx+1, depth+1, choice, combi, len_combi, dfs_result, final)
    dfs_result.pop()


def calculate(start_p, end_p):
    start_y, start_x = start_p
    end_y, end_x = end_p
    return abs(end_y-start_y) + abs(end_x-start_x)

def solution(N, maps):
    visited = [[False]*N for _ in range(N)]
    map_check = {}
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    min_result = float("inf")
    boundary = {}

    """
    1. 섬 탐색
    """
    idx = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                idx += 1
                queue = deque([(i, j)])
                boundary.setdefault(idx, [])

                while queue:
                    start_y, start_x = queue.popleft()
                    # 맵도 id로 바꿔놓기
                    maps[start_y][start_x] = idx
                    map_check.setdefault(idx, set()).add((start_y, start_x))
                    visited[start_y][start_x] = True
                    edge_flag = False

                    for dy, dx in directions:
                        ny, nx = start_y+dy, start_x+dx
                        if 0 <= ny < N and 0 <= nx < N:
                            if maps[ny][nx] == 0:
                                edge_flag = True
                            elif not visited[ny][nx]:
                                queue.append((ny, nx))
                                visited[ny][nx] = True

                    if edge_flag:
                        boundary[idx].append((start_y, start_x))


    """
    2. 경계면에서 바다로 탐색
    """
    #pprint(maps)
    #print(boundary)

    visited_dict = {i: [[False]*N for _ in range(N)] for i in range(1, idx+1)}
    queue = deque()
    # 모든 섬의 경계를 큐에 넣기
    # 한번에 다 넣고 각 지점에서 턴 식으로 찾으면 최소 거리 딱 한개만 나옴
    for island_id in boundary:
        for y, x in boundary[island_id]:
            queue.append((0, island_id, y, x))

    while queue:
        dis, cur_id, start_y, start_x = queue.popleft()
        for dy, dx in directions:
            ny, nx = start_y+dy, start_x+dx
            if 0 <= ny < N and 0 <= nx < N:
                if cur_id != maps[ny][nx] and maps[ny][nx] != 0:
                    return dis

                elif maps[ny][nx] == 0 and not visited_dict[cur_id][ny][nx]:
                    visited_dict[cur_id][ny][nx] = True
                    queue.append((dis+1, cur_id, ny, nx))


if __name__ == "__main__":
    from collections import deque
    import sys
    sys.setrecursionlimit(10**7)

    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))

    print(solution(N, maps))