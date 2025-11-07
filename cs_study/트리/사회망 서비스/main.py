from collections import deque
import sys
sys.setrecursionlimit(10**7)

def dfs(cur, min_dp, visited, adj_dict):
    visited[cur] = True
    min_dp[cur][0] = 0
    min_dp[cur][1] = 1

    for nxt in adj_dict[cur]:
        if not visited[nxt]:
            dfs(nxt, min_dp, visited, adj_dict)
            min_dp[cur][0] += min_dp[nxt][1]
            min_dp[cur][1] += min(min_dp[nxt][0], min_dp[nxt][1])

def solution(N, adj_dict):
    """
    [조건]
    무방향 그래프이기에 visited를 고려해야한다
    최솟값을 구하는 경우이기에 dp를 적용해야한다.
    자신이 얼리어답터이냐, 아니냐에 따라 가짓수가 달라지므로 dfs를 고려한다.
    그리고 dfs를 통해 후위순회부터 진행해서 거슬러 올라가 상위노드로 전달되어야함

    얼리어답터 여부를 판단하기 위해 dp의 값은 한자리만이 아닌
    [0,0]와 같이 2개의 값을 받는다.

    """
    visited = [False] * (N+1)
    min_dp = [[0, 0] for _ in range(N+1)]
    dfs(1, min_dp, visited, adj_dict)
    return min(min_dp[1][0], min_dp[1][1])


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    adj_dict = {
        node: [] for node in range(1, N+1)
    }
    for _ in range(N-1):
        a, b = map(int, input().split())
        adj_dict[a].append(b)
        adj_dict[b].append(a)

    print(solution(N, adj_dict))

