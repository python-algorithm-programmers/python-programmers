def solution(a, b):
    N, M = len(a), len(b)
    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]+1

            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j-1]
                )
    #print(dp)
    return dp[N][M]


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    a = input().strip()
    b = input().strip()
    print(solution(a, b))