def solution(N, adj_dict):
    indegree = {i: 0 for i in range(1, N+1)}
    for node in adj_dict['adj']:
        for nxt in adj_dict['adj'].get(node):
            indegree[nxt] += 1
    adj_dict['indegree'] = indegree

    # 시작점 뽑기
    queue = deque()
    for node in adj_dict['adj']:
        if indegree[node] == 0:
            queue.append(node)

    result = []
    #print(adj_dict['adj'])
    #print(adj_dict['indegree'])
    while queue:
        cur = queue.popleft()
        result.append(cur)
        for nxt in adj_dict['adj'][cur]:
            adj_dict['indegree'][nxt] -= 1
            if adj_dict['indegree'][nxt] == 0:
                queue.append(nxt)

    if len(result) != N:
        print(0)
        return

    for a in result:
        print(a)


if __name__ == "__main__":
    import sys
    import heapq
    from collections import deque

    input = sys.stdin.readline
    N, M = map(int, input().split())
    adj_dict = {}
    adj = {i: [] for i in range(1, N+1)}
    indegree = {}
    adj_dict['indegree'] = indegree
    for _ in range(M):
        input_list = list(map(int, input().split()))
        n = input_list[0]

        for i in range(1, n):
            a = input_list[i]
            b = input_list[i+1]
            adj.setdefault(a, []).append(b)

    adj_dict['adj'] = adj
    solution(N, adj_dict)