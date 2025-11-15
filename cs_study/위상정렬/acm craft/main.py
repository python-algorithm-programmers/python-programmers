from collections import deque


def solution(adj, indegree_dict, win, time_list, N):
    time_dp = [0] * (N + 1)

    # 시작점 찾기
    t_q = deque()
    for inde_k in indegree_dict:
        if indegree_dict[inde_k] == 0:
            t_q.append(inde_k)
            time_dp[inde_k] = time_list[inde_k]

    while t_q:
        cur = t_q.popleft()
        for nxt in adj[cur]:
            time_dp[nxt] = max(time_dp[nxt], time_dp[cur]+time_list[nxt])
            indegree_dict[nxt] -= 1
            if indegree_dict[nxt] == 0:
                t_q.append(nxt)

    return time_dp[win]


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        time_list = list(map(int, input().split()))
        time_list.insert(0, 0)
        adj = {
            node: [] for node in range(1, N + 1)
        }
        indegree_dict = {
            node: 0 for node in range(1, N + 1)
        }

        for _ in range(K):
            a, b = map(int, input().split())
            adj[a].append(b)

        for key in adj:
            for nxt in adj[key]:
                indegree_dict[nxt] += 1

        win = int(input())
        print(solution(adj, indegree_dict, win, time_list, N))