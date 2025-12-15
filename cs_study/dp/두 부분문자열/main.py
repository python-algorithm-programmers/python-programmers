def pprint(arr):
    for row in arr:
        print(row)

def solution(input_a, input_b):
    # 공통 문자열의 갯수의 최댓값을 빼주면 됨
    # LCS의 공통 문자열과, 수열 중에서 공통문자열로 풀기
    a = len(input_a)
    b = len(input_b)
    dp = [[0]*(b+1) for _ in range(a+1)]

    max_one = 0
    for i in range(1, a+1):
        for j in range(1, b+1):
            if input_a[i-1] == input_b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_one = max(dp[i][j], max_one)
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    #pprint(dp)
    return a+b - max_one


if __name__ == "__main__":
    input_a = input()
    input_b = input()
    print(solution(input_a, input_b))