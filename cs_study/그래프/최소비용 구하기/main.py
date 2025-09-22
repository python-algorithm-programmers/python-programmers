def solution(N, M, bus_dict, start, end):
    INF = 10 ** 9
    dist = [INF] * (N+1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        total_cost, cur_city = heapq.heappop(pq)
        # if cur_city == end:
        #     return total_cost

        # 거르기
        if total_cost > dist[cur_city]:
            continue

        # 버스가 지나가는 지 확인
        if bus_dict.get(cur_city):
            for next, cost in bus_dict[cur_city]:
                next_cost = total_cost + cost
                if dist[next] > next_cost:
                    dist[next] = next_cost
                    heapq.heappush(pq, (next_cost, next))

    return dist[end]


if __name__ == "__main__":
    import heapq
    N = int(input())
    M = int(input())
    bus_dict = {}
    for _ in range(M):
        u, v, cost = map(int, input().split())
        # 단방향
        bus_dict.setdefault(u, []).append((v, cost))
    start, end = map(int, input().split())
    print(solution(N, M, bus_dict, start, end))
