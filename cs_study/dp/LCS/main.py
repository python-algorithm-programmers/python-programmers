def solution(line1, line2):
    n = len(line1)
    m = len(line2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    #print(dp)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if line1[i-1] == line2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m] - 1



if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    line1 = input()
    line2 = input()
    print(solution(line1, line2))