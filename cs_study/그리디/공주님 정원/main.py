def day_maker(m, d):
    return m*100 + d

def solution(N, flower_maps):
    dp = [N]*N
    # END는 그 날짜는 빼므로 12월 1일가지 필요
    START, END = 301, 1201

    # 3월 1일 이하는 1개로 시작
    for i in range(N):
        smi, sdi, emi, edi = flower_maps[i]
        if day_maker(smi, sdi) <= 301:
            dp[i] = 1

    for i in range(N):
        smi, sdi, emi, edi = flower_maps[i]
        for j in range(i):
            smj, sdj, emj, edj = flower_maps[j]
            if day_maker(emj, edj) >= day_maker(smi, sdi):
                dp[i] = min(dp[i], dp[j]+1)

    answer = min((dp[i] for i in range(N) if day_maker(flower_maps[i][2], flower_maps[i][3]) >= END))
    return answer


if __name__ == "__main__":
    import sys
    flower_maps = []
    N = int(sys.stdin.readline().strip())
    for _ in range(N):
        line = list(map(int, sys.stdin.readline().strip().split()))
        start_month, start_day, end_month, end_day = line[0], line[1], line[2], line[3]
        # 솎아내기
        if 3<=end_month and start_month<=11:
            flower_maps.append((start_month, start_day, end_month, end_day))

    # 정렬
    flower_maps.sort(key=lambda x: (x[0], x[1], -(x[2] * 100 + x[3])))
    print(solution(N, flower_maps))