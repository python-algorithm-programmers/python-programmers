from collections import deque


def solution(tickets):
    adj = {
        ticket[0]: [] for ticket in tickets
    }

    for ticket in tickets:
        adj[ticket[0]].append(ticket[1])

    # 정렬
    for key in adj:
        adj[key].sort()

    print(adj)
    answer = []

    def dfs(cur):
        answer.append(cur)
        if not adj.get(cur):
            return

        while adj[cur]:
            nxt = adj[cur].pop(0)
            dfs(nxt)

    dfs("ICN")
    print(adj)
    return answer