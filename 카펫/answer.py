def getDivisor(n):
    divisor_list = []
    for i in range(1, int(n**(1/2)+1)):
        if n%i == 0:
            divisor_list.append(i)
            divisor_list.append(n//i)

    divisor_list.sort()
    return divisor_list
def solution(brown, yellow):

    # 전체 더한 것의 약수를 구하기
    divisor_list = getDivisor(brown+yellow)

    # 구한 약수의 세트에 2를 빼서 쌍의 곱이 yellow인 지 확인
    if len(divisor_list) % 2 == 0:
        left_idx = len(divisor_list) // 2 - 1
        right_idx = len(divisor_list) // 2

    else:
        left_idx = len(divisor_list) // 2
        right_idx = len(divisor_list) // 2

    answer = []
    while True:
        if (divisor_list[left_idx]-2) * (divisor_list[right_idx]-2) == yellow:
            answer.append(divisor_list[right_idx])
            answer.append(divisor_list[left_idx])
            return answer

        else:
            left_idx -= 1
            right_idx += 1

if __name__ == '__main__':
    print(solution(24, 24))
