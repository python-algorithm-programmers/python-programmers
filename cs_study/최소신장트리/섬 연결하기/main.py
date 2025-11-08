"""
최소 간선의 비용과 간선으로 사이클 없이 하나의 네트워크를 구축 = 최소 신장 트리
프림 알고리즘 기반, 임의의 노드에서 시작해도 상관없음
"""
import heapq


def solution(n, costs):
    adj_dict = {
        node: [] for node in range(n)
    }
    for a, b, cost in costs:
        adj_dict[a].append((cost, b))
        adj_dict[b].append((cost, a))

    visited = [False] * n
    # 간선의 수
    cnt = 0
    answer = 0
    # 비용, 노드 순으로
    heap_list = [(0, 0)]
    while heap_list and cnt < n:
        cost, cur = heapq.heappop(heap_list)
        if not visited[cur]:
            visited[cur] = True
            cnt += 1
            answer += cost

            for nxt_cost, nxt in adj_dict[cur]:
                if not visited[nxt]:
                    heapq.heappush(heap_list, (nxt_cost, nxt))

    return answer