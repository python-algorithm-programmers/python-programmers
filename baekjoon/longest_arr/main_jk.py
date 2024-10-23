
def solution(N, number_list):
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            # 한 지점에 대해, 그 지점 이하의 수를 조회하고 더 작은 수가 나올 때마다
            if number_list[i] > number_list[j]:
                # for문 돌면서 만들었던거 리로드하는 작업이
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)


if __name__ == "__main__":
    import sys
    lines = sys.stdin.readlines()
    N = lines[0].strip()
    numbers = list(map(int, lines[1].strip().split(" ")))
    print(solution(int(N), numbers))