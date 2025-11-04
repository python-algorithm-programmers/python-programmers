from collections import deque
import heapq
def solution(N, adj):
    indegree_dict = {
       node: 0 for node in range(1, N+1)
    }

    result = []
    queue = []
    for indegree_key in indegree_dict:
        for nxt in adj.get(indegree_key, []):
            indegree_dict[nxt] += 1

    for indegree_key in indegree_dict:
        if indegree_dict[indegree_key] == 0:
            heapq.heappush(queue, indegree_key)

    result.sort()
    # print(indegree_dict)
    # print(adj)
    # print(queue)
    # print()

    while queue:
        cur = heapq.heappop(queue)
        result.append(cur)

        for nxt in adj.get(cur, []):
            indegree_dict[nxt] -= 1
            if indegree_dict[nxt] == 0:
                heapq.heappush(queue, nxt)

    return " ".join(map(str, result))


if __name__ == "__main__":
    N, M = map(int, input().split())
    adj = {}
    for _ in range(M):
        k, v = map(int, input().split())
        adj.setdefault(k, []).append(v)

    print(solution(N, adj))
