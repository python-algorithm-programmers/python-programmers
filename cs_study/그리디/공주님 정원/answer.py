def solution(N, flower_maps):
    # 날짜를 비교하기 쉽게 MMDD 정수로
    def to_day(m, d):
        return m*100 + d

    START = 301   # 3/01
    END   = 1201  # 12/01 (11/30까지 덮이면 OK)
    INF   = 10**9

    # 필터링 때문에 N이 줄었을 수 있으니 실제 길이로
    N = len(flower_maps)

    answer = []          # (원래 변수 유지)
    dp = [INF]*N         # ★ 최소값 DP는 INF로 초기화

    # 시작점(3/1 이전 또는 당일 시작)은 1개로 시작
    for i in range(N):
        smi, sdi, emi, edi = flower_maps[i]
        if to_day(smi, sdi) <= START:
            dp[i] = 1

    # 전이: j < i, j의 끝이 i의 시작을 덮으면 dp[i] = min(dp[i], dp[j]+1)
    for i in range(N):
        smi, sdi, emi, edi = flower_maps[i]
        for j in range(i):
            smj, sdj, emj, edj = flower_maps[j]
            if dp[j] == INF:
                continue
            if to_day(emj, edj) >= to_day(smi, sdi):
                dp[i] = min(dp[i], dp[j] + 1)

    # 11/30 이후까지(= END 이상) 덮는 구간 중 최소 개수
    ans = INF
    for i in range(N):
        smi, sdi, emi, edi = flower_maps[i]
        if to_day(emi, edi) >= END:
            ans = min(ans, dp[i])

    return 0 if ans == INF else ans

if __name__ == "__main__":
    import sys
    flower_maps = []
    N = int(input())
    for _ in range(N):
        line = list(map(int, input().split()))
        start_month, start_day, end_month, end_day = line[0], line[1], line[2], line[3]
        # 솎아내기
        if 3<=end_month and start_month<=11:
            flower_maps.append((start_month, start_day, end_month, end_day))

    # 정렬
    flower_maps.sort(key=lambda x:(x[0], -x[2]))
    print(solution(N, flower_maps))