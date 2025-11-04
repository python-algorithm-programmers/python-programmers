from collections import deque


def solution(N, adj):
    indegree_dict = {
       node: 0 for node in range(1, N+1)
    }
    queue = deque()
    result = []
    for indegree_key in indegree_dict:
        for nxt in adj.get(indegree_key, []):
            indegree_dict[nxt] += 1

    for k in indegree_dict:
        if indegree_dict[k] == 0:
            queue.append(k)
            result.append(k)

    # print(indegree_dict)
    # print(queue)
    while queue:
        cur = queue.popleft()
        for nxt in adj.get(cur, []):
            indegree_dict[nxt] -= 1

            if indegree_dict[nxt] == 0:
                queue.append(nxt)
                result.append(nxt)

    return " ".join(map(str, result))


if __name__ == "__main__":
    N, M = map(int, input().split())
    adj = {}
    for _ in range(M):
        key, value = map(int, input().split())
        adj.setdefault(key, []).append(value)

    print(solution(N, adj))