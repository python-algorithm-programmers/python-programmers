def solution(N, little_num):
    result = 0
    start = end = 0
    sum_arr = little_num[end]
    while end < len(little_num):
        if sum_arr > N:
            sum_arr -= little_num[start]
            start += 1
            continue

        elif sum_arr == N:
            result += 1

        end += 1
        if end == len(little_num):
            break

        sum_arr += little_num[end]
    return result

if __name__ == "__main__":
    N = int(input())
    num_arr = [0]*(N+1)

    # 에라토스 체
    for i in range(1, N+1):
        for j in range(i, N+1, i):
            num_arr[j] += 1

    little_num = []
    for i in range(2, N+1):
        if num_arr[i] == 2:
            little_num.append(i)

    print(solution(N, little_num))
