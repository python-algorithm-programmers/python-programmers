"""
다익스트라 문제
heap으로 최소 거리를 가진 노드로 판별하도록 해야함
[(거리, 노드)]로 판독
"""
from collections import deque
import heapq


def solution(N, road, K):
    adj_dict = {
        node: [] for node in range(1, N + 1)
    }
    for a, b, dis in road:
        adj_dict[a].append([b, dis])
        adj_dict[b].append([a, dis])

    dist = [float("inf")] * (N + 1)
    dist[1] = 0
    heap_list = [(0, 1)]
    while heap_list:
        cur_dis, cur = heapq.heappop(heap_list)
        if cur_dis > dist[cur]:
            continue
        for nxt, cost in adj_dict[cur]:
            final_distance = cost + dist[cur]
            if dist[nxt] > final_distance:
                dist[nxt] = final_distance
                heapq.heappush(heap_list, ((final_distance, nxt)))

    return sum(1 for a in dist if a <= K)