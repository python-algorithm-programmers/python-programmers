from collections import deque

def solution(adj, tour_list):
    visited = [False]*(N+1)
    start_p = tour_list[0]
    queue = deque([start_p])

    while queue:
        node = queue.popleft()
        visited[node] = True
        for nxt in adj[node]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

    for tour in tour_list:
        if not visited[tour]:
            return "NO"
    return "YES"

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    adj = [[] for _ in range(N+1)]

    for i in range(1, N+1):
        input_list = list(map(int, input().strip().split()))
        for j in range(len(input_list)):
            if input_list[j] == 1:
                adj[i].append(j+1)

    tour_list = list(map(int, input().strip().split()))
    print(solution(adj, tour_list))

