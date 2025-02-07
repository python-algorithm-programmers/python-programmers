def solution(N):
    result = [0]*(N+1)

    # 초기값 설정
    result[0] = 4
    if N >= 1:
        result[1] = 9

    # 점화식 기반
    for i in range(2, N+1):
        result[i] = 4 * result[i-1] -4*(2*(i-1)+1)+1

    return result[N]


if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline().strip())
    print(solution(N))