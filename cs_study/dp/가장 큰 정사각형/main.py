def solution(n, m, box_lines):
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if box_lines[i-1][j-1] == 1:
                square = 1
                # 왼, 위, 왼대각선이 존재하는 경우
                # 얘네도 존재하는 거면 앞단계에서 이미 정사각형 여부를 판단
                if i >= 2 and j >= 2:
                    if box_lines[i-2][j-2] == 1 and box_lines[i-2][j-1] == 1 and box_lines[i-1][j-2] == 1:
                        square = dp[i-1][j-1] + 1

                dp[i][j] = max(dp[i-1][j], dp[i][j-1], square)

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m] ** 2

if __name__ == "__main__":
    n, m = map(int, input().split())
    box_lines = []
    for _ in range(n):
        box_line = list(map(int, input().strip()))
        box_lines.append(box_line)
    print(solution(n, m, box_lines))
