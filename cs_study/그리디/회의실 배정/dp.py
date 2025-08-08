import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    input_points = []
    for _ in range(N):
        start, end = map(int, sys.stdin.readline().split())
        input_points.append([start, end])

    # 시작 시간 기준으로 정렬
    input_points.sort(key=lambda x:(x[0], x[1]))

    # 해당 단계에서 예약할 수 있는 회의실의 최대 수
    dp = [1]*N

    for i in range(N):
        si, ei = input_points[i]
        for j in range(i):
            sj, ej = input_points[j]

            if ej <= si:
                dp[i] = max(dp[i], dp[j]+1)

    print(max(dp))