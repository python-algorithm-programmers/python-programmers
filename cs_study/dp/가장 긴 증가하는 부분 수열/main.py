def solution(N, numbers):
    # bottom-up 방식
    # 자리에 놓인 값을 설정할 배열
    dp = [1]*N

    # 현재 위치에 놓일 값의 최댓값은 이전 값에 영향을 받음
    # 그리고 배열에 저장될 값은 최댓값이 되도록 설정해야
    # 다음 위치에 놓일 값도 최댓값이 보장됨
    for i in range(N):
        for j in range(i):
            if numbers[j] < numbers[i]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)


if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    numbers = list(map(int, line.split(" ")))
    print(solution(N, numbers))
