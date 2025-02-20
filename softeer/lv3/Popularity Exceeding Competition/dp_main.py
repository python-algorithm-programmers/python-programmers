def solution(N, input_data):
    dp = [0]*(N+1)
    max_popularity = 0

    for i in range(N):
        P, C = input_data[i]

        for j in range(i,-1,-1):
            if abs(P-max_popularity) <= C:
                dp[j+1] = max(dp[j+1], dp[j]+1)
                max_popularity = max(max_popularity, dp[j+1])

    return max_popularity

if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline().strip())
    input_data = [tuple(map(int, sys.stdin.readline().split(" "))) for __ in range(N)]
    print(solution(N, input_data))