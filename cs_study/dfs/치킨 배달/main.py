import sys
sys.setrecursionlimit(100000)
def distance(maps, points):
    dist_list = [[2500]*N for _ in range(N)]
    for point in points:
        for i in range(N):
            for j in range(N):
                if maps[i][j] == 1:
                    point_y, point_x = point
                    dist = abs(point_y-i) + abs(point_x-j)
                    dist_list[i][j] = min(dist, dist_list[i][j])

    final_list = []
    for r in range(N):
        for c in range(N):
            if dist_list[r][c] != 2500:
                final_list.append(dist_list[r][c])
    return sum(final_list)


def dfs(idx, cnt, best, maps, points, M, chicken_maps):
    if cnt == M:
        # 거리 계산
        cur_dis = distance(maps, points)
        best[0] = min(cur_dis, best[0])
        return

    if idx == len(chicken_maps):
        return

    # 여기서 치킨 집 안 고르고 다음꺼로 넘어감
    dfs(idx+1, cnt, best, maps, points, M, chicken_maps)

    # 치킨집 고르고 트리 더 깊이 들어감
    cur_y, cur_x = chicken_maps[idx]
    if maps[cur_y][cur_x] == 2:
        points.append((cur_y, cur_x))
        dfs(idx + 1, cnt+1,  best, maps, points, M, chicken_maps)
        points.pop()

def solution(N, M, maps):
    points = []
    best = [2500]
    chicken_maps = [
        (i, j)
        for i in range(N)
        for j in range(N)
        if maps[i][j] == 2
    ]
    dfs(0, 0, best, maps, points, M, chicken_maps)
    return best[0]


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, sys.stdin.readline().strip().split())))
    print(solution(N, M, maps))