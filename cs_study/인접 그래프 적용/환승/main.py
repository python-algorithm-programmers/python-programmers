def solution(N, adj_dict):
    end = N
    INF = 10 ** 9
    dist = [INF] * (N+1)
    pq = [] # (turn, city)
    heapq.heappush(pq, (1, 1))
    while pq:
        total_cost, cur_city = heapq.heappop(pq)

        # 거르기
        if dist[cur_city] < total_cost:
            continue

        for next_city in adj_dict[cur_city]:
            next_cost = total_cost + 1
            if dist[next_city] > next_cost:
                dist[next_city] = next_cost
                heapq.heappush(pq, (next_cost, next_city))

    return dist[end]


if __name__ == "__main__":
    import heapq
    N, K, M = map(int, input().split())
    # adj = [[0]*(N+1) for _ in range(N+1)]
    adj_dict = {}
    for _ in range(M):
        line = list(map(int, input().strip().split()))
        for u in range(K):
            for v in range(u+1, K):
                adj_dict.setdefault(line[u], []).append(line[v])
                adj_dict.setdefault(line[v], []).append(line[u])
    print(solution(N, adj_dict))



