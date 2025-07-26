
def dfs(cur_dis, cur, destination):
    if cur == destination:
        return cur_dis
    visited[cur] = True
    for next, distance in adjacent_metrix[cur]:
        if not visited[next]:
            sum_distance = dfs(cur_dis+distance, next, destination)
            if sum_distance != 10001:
                return sum_distance

    return 10001


if __name__ == "__main__":
    N, M = map(int, input().split())
    adjacent_metrix = [[] for _ in range(N+1)]
    for _ in range(N-1):
        start, end, distance = map(int, input().split())
        adjacent_metrix[start].append((end, distance))
        adjacent_metrix[end].append((start, distance))

    for _ in range(M):
        visited = [False] * (N+1)
        start_p, end_p = map(int, input().split())
        total_distance = dfs(0, start_p, end_p)
        print(total_distance)