def solution(N, K, bag_list):
    # i번째 물건까지 고려했을 대, 무게 j 한도에서 얻을 수 있는 최대 가치
    dp = [[0]*(K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        w, v = bag_list[i-1]
        for j in range(1, K+1):
            # 한도 넘음
            if j < w:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i-1][j-w] + v
                )

    return max(dp[N])



if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    bag_list = []
    for _ in range(N):
        W, V = map(int, input().split())
        bag_list.append((W, V))

    print(solution(N, K, bag_list))
