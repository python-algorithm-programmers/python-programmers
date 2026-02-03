"""
모든 u, v에 대해 u 또는 v는 얼리어답터이어야
모두 자식 노드들에 친구가 됨

부모나 자식 중 하나는 얼리어답터야함
"""
def solution(N, adj_dict):
    """
    dp 정의
    노드 u가 얼리어답터가 아닐 때,
    u를 루트로 하는 하위트리에서 필요한 최소 얼리어답터 수

    노드 u가 얼리어답터일 때,
    u를 루트로 하는 하위트리에서 필요한 최소 얼리어답터 수
    """
    # 부모에서 얼리어답터를 먼저 결정하는 식
    # 그래서 그 다음 하위 트리 노드가 얼리어답터 고려 안해도 될지 말지 판단

    # dp[u][0] -> 현재 노드가 얼리어답터일 때, 최소 누적 얼리어답터 수
    # dp[u][1] -> 현재 노드가 얼리어답터가 아니여서 자식 노드 누적 얼리어답터 더하기
    dp = [[0, 0] for _ in range(N+1)]

    # 트리구조 쓰기
    visited = [False] * (N+1)

    def dfs(u):
        visited[u] = True
        dp[u][0] = 1
        dp[u][1] = 0
        #print(adj_dict)

        for v in adj_dict.get(u, []):
            if not visited[v]:
                visited[v] = True
                dfs(v)

                # 현재 노드가 얼리어답터가 아니어서 자식 노드 얼리어답터일 때의 경우의 수 더함
                dp[u][1] += dp[v][0]

                # 현재 노드가 얼리어답터이면
                dp[u][0] += min(dp[v])

    dfs(1)
    return min(dp[1])

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**8)
    input = sys.stdin.readline

    N = int(input())
    adj_dict = {}
    for _ in range(N-1):
        u, v = map(int, input().split())
        adj_dict.setdefault(u, []).append(v)
        adj_dict.setdefault(v, []).append(u)

    print(solution(N, adj_dict))