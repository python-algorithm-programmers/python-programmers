def solution(n, m, box_lines):
    dp = [[0]*(m+1) for _ in range(n+1)]
    answer = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if box_lines[i-1][j-1] == 1:
                dp[i][j] = min(
                    dp[i-1][j],
                    dp[i][j-1],
                    dp[i-1][j-1]
                ) + 1
                answer = max(answer, dp[i][j])

            else:
                # box가 0이면 여기를 오른쪽 아래로 하는 정사각형은 없다
                dp[i][j] = 0

    print(dp)
    return answer * answer

if __name__ == "__main__":
    n, m = map(int, input().split())
    box_lines = []
    for _ in range(n):
        box_line = list(map(int, input().strip()))
        box_lines.append(box_line)
    print(solution(n, m, box_lines))