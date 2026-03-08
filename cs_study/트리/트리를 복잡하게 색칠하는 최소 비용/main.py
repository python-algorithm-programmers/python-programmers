def dfs(cur, indegree_dict, wb_cost, dp):
    white_cost, black_cost = wb_cost[cur]
    dp[cur][0] = white_cost
    dp[cur][1] = black_cost

    for nxt in indegree_dict.get(cur, []):
        dfs(nxt, indegree_dict, wb_cost, dp)

        # 백트래킹 되는 첫 순간이 리프노드
        dp[cur][0] += min(dp[nxt][0], dp[nxt][1])
        dp[cur][1] += dp[nxt][0]


def solution(n, indegree_dict, wb_cost):
    # 트리 dp 유형
    # 즉시 특정 정점에 black으로 두는 게 싸보여도
    # 그 선택에 자식 노드의 white를 장제해서
    # 서브트리 비용이 올바르지 않을 수 있음

    # dp 정의
    """
    dp[node][0] = node를 white로 칠했을 때,
    node를 루트로 하는 서브트리 전체를 조건에 맞게 최소 비용

    dp[node][1] = node를 black으로 칠햇을 때

    리프가지 탐색하고 나서, 백트래킹으로 비용을 추산하는 형태여야합니다.
    """

    dp = [[0, 0] for _ in range(n)]
    dfs(0, indegree_dict, wb_cost, dp)
    return min(dp[0][0], dp[0][1])


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline


    n = int(input())
    indegree_dict = {}
    for _ in range(n-1):
        p, c = input().split()
        p, c = int(p), int(c)
        indegree_dict.setdefault(p, []).append(c)

    wb_cost = {}
    for i in range(n):
        w, b = input().split()
        w, b = int(w), int(b)
        wb_cost[i] = (w, b)

    print(solution(n, indegree_dict, wb_cost))