def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    else:
        # 피보나치 수열이고 동적프로그래밍으로도 가능
        dinamic_pibo = [0]*(n+1)

        # 초기 조건
        dinamic_pibo[1] = 1
        dinamic_pibo[2] = 2

        for i in range(3, n+1):
            dinamic_pibo[i] = dinamic_pibo[i-1] + dinamic_pibo[i-2]

        return dinamic_pibo[n] % 1234567

if __name__ == '__main__':
    print(solution(6))