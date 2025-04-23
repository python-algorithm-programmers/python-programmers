def solution(N, elec_line):
    # LIS 적용
    dp = [1]*N
    for i in range(N):
        for j in range(i):
            if elec_line[j][1] < elec_line[i][1]:
                dp[i] = max(dp[i], dp[j]+1)

    return N - max(dp)

if __name__ == "__main__":
    import sys
    lines = sys.stdin.readlines()
    N = int(lines[0])
    elec_line = []
    for line in lines[1:]:
        elec_line.append(list(map(int, line.strip().split(" "))))

    # 정렬
    elec_line.sort(key=lambda x:x[0])
    print(solution(N, elec_line))