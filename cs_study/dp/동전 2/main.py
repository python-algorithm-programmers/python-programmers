def solution(n, k, money_list):
    dp = [100001]*(k+1) # 0~k까지
    dp[0] = 0
    #print(money_list)

    # bottom up으로 시작
    for t in range(1, k+1):
        for money in money_list:
            if t - money >= 0:
                # t-money 상태에서 동전 1개를 써서 현재 돈까지 맞춘 경우
                dp[t] = min(dp[t-money]+1, dp[t])

    # print(dp)
    return dp[k] if dp[k] != 100001 else -1

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    money_list = []
    n, k = map(int, input().split())
    for _ in range(n):
        money_list.append(int(input()))

    money_list.sort(reverse=True)
    print(solution(n, k ,money_list))
