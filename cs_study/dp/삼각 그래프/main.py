def solution(r, maps):
    dp = [[9999999]*4 for _ in range(r+1)]
    # 초기화
    dp[1][1] = 9999999
    dp[1][2] = maps[0][1]
    dp[1][1] = maps[0][1] + maps[0][2]
    #print(maps)

    for i in range(2, r+1):
        dp[i][1] = maps[i-1][0] + min(
            dp[i-1][1], dp[i-1][2]
        )

        dp[i][2] = maps[i - 1][1] + min(
            dp[i - 1][1], dp[i - 1][2], dp[i - 1][3], dp[i][1]
        )

        dp[i][3] = maps[i - 1][2] + min(
            dp[i - 1][2], dp[i - 1][3], dp[i][2]
        )

    return dp[r][2]

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    case = 1
    while True:
        N = int(input())
        r = N
        maps = []
        for _ in range(N):
            input_list = list(map(int, input().split()))
            maps.append(input_list)

        answer = solution(r, maps)
        print(f"{case}. {answer}")
        end = int(input())
        if end == 0:
            break

        case += 1
