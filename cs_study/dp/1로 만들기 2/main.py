def solution(N):
    # bottom-up 방식
    # 최솟값으로 쌓아가는 형태, 각 인덱스 별 최솟값을 저장할 배열 선언
    dp = [0]*(N+1)

    # 이전 값 저장하는 배열
    past = [0]*(N+1)

    # 1은 0이므로 2부터 시작
    for i in range(2,N+1):
        # -1은 항상 어느 단계에서 수행할 수 있으므로 먼저 검사
        dp[i] = dp[i-1]+1
        past[i] = i-1

        # 2로 나눠 떨어지면서, 이전꺼+1이 현재보다 더 작은 경우
        if i%2 == 0 and dp[i//2]+1 < dp[i]:
            dp[i] = dp[i//2] + 1
            past[i] = i//2

        # 3으로 나눠 떨어지면서, 이전꺼+1이 현재보다 더 작은 경우
        if i%3 == 0 and dp[i//3]+1 < dp[i]:
            dp[i] = dp[i//3] + 1
            past[i] = i//3

    # 경로 복원
    path = []
    check_point = N
    while True:
        if check_point == 1:
            break
        path.append(past[check_point])
        check_point = past[check_point]

    print(dp[N])
    print(path)

if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline().strip())
    solution(N)