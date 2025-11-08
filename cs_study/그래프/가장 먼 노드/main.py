from collections import deque


def solution(n, vertex):
    adj_dict = {
        node: [] for node in range(1, n + 1)
    }
    indegree_dict = {
        node: 0 for node in range(1, n + 1)
    }

    for start, end in vertex:
        adj_dict[start].append(end)
        adj_dict[end].append(start)

    visited = [False] * (n + 1)

    queue = deque([1])
    while queue:
        cur = queue.popleft()
        visited[cur] = True
        for nxt in adj_dict[cur]:
            if not visited[nxt]:
                indegree_dict[nxt] += indegree_dict[cur] + 1
                visited[nxt] = True
                queue.append(nxt)

    indegree_list = sorted(list(indegree_dict.items()), key=lambda x: -x[1])
    max_vertex = indegree_list[0][1]
    answer = 0
    for node, price in indegree_list:
        if price == max_vertex:
            answer += 1
        else:
            break

    # print(indegree_list)
    return answer