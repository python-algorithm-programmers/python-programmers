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
    boundary = {}
    new_maps = [arr[:] for arr in maps]

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
                    new_maps[start_y][start_x] = idx
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

    #pprint(new_maps)
    """
    2. 경계면에서 각기 큐로 바다로 탐색
    """
    #pprint(maps)
    #print(boundary)
    #visited_dict = {i: [[False]*N for _ in range(N)] for i in range(1, idx+1)}

    # 모든 섬의 경계를 큐에 넣기
    # 한번에 다 넣고 각 지점에서 턴 식으로 찾으면 최소 거리 딱 한개만 나옴
    queue = deque()
    INF = N*N
    answer = INF

    # 해당 섬에서 시작해서, 바다 칸을 몇 칸 지나 현재 칸에 도달했는 가
    dist = [[INF]*N for _ in range(N)]
    for island_id in boundary:
        for y, x in boundary[island_id]:
            queue.append((y, x))
            dist[y][x] = 0

    while queue:
        start_y, start_x = queue.popleft()
        for dy, dx in directions:
            ny, nx = start_y+dy, start_x+dx
            if 0 <= ny < N and 0 <= nx < N:
                # 바다면서 아직 방문 안함
                if new_maps[ny][nx] == 0 and dist[ny][nx] == INF:
                    dist[ny][nx] = dist[start_y][start_x] + 1
                    # 각 큐가 다음 접근 바다 영역에 대해 자기 영역으로 지정
                    new_maps[ny][nx] = new_maps[start_y][start_x]
                    queue.append((ny, nx))

                # 누가 방문해온 곳에 마주한 경우
                elif new_maps[ny][nx] != new_maps[start_y][start_x]:
                    answer = min(answer, dist[ny][nx]+dist[start_y][start_x])

    #print("after")
    #pprint(new_maps)
    return answer


if __name__ == "__main__":
    from collections import deque
    import sys
    sys.setrecursionlimit(10**7)

    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))

    print(solution(N, maps))