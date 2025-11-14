"""
1. 중간지점까지 다익스트라로 도달 거리 dist 설정
2. for문으로 각 노드로 시작점 정해서 다시 다이스트라 적용하는 데, A+B의 거리합이 최소 되는 것을 찾기
결국, 이중 다익스트라 적용
"""
import heapq


def solution(n, s, a, b, fares):
    # 다익스트라로 중간지점까지의 최소 거리 확보
    dist = [float("inf")] * (n + 1)
    dist[s] = 0
    adj = {
        node: [] for node in range(1, n + 1)
    }
    for start, end, cost in fares:
        adj[start].append((cost, end))
        adj[end].append((cost, start))

    heap_list = [(0, s)]
    while heap_list:
        cur_dis, cur = heapq.heappop(heap_list)
        for cost, nxt in adj[cur]:
            final_dis = cur_dis + cost
            if final_dis < dist[nxt]:
                dist[nxt] = final_dis
                heapq.heappush(heap_list, (final_dis, nxt))

    # 중간 지점에서 A, B까지 얼마나 소요될지를 측정
    start_points = {i for i in range(1, n + 1)}
    # start_points.remove(s)

    answer = float("inf")
    # start_p 기준으로 다시 다익스트라 적용
    for start_p in list(start_points):
        distance = dist[start_p]
        second_dist = [float("inf")] * (n + 1)
        second_dist[start_p] = 0

        new_heap_list = [(0, start_p)]
        while new_heap_list:
            cur_dis, cur = heapq.heappop(new_heap_list)
            for cost, nxt in adj[cur]:
                final_dis = cur_dis + cost
                if final_dis < second_dist[nxt]:
                    second_dist[nxt] = final_dis
                    heapq.heappush(new_heap_list, (final_dis, nxt))

        # A, B까지의 거리합
        total_dis = second_dist[a] + second_dist[b] + distance
        if answer > total_dis:
            answer = total_dis

        # print(dist)
        # print(start_p, second_dist)
        # print(answer)
        # print()

    return answer