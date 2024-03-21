# 10진수를 n진법 수로 표현하는 메서드
def decimal_to_base_n(number, base_n):
    num_list = []
    while number >= base_n:
        if number % base_n < 10:
            num_list.append(str(number % base_n))

        # 만약 10진수 이상이며, 나머지가 10이상이면
        # 영문자 반환
        else:
            plus_number = number % base_n - 10
            str_num = chr(ord('A')+plus_number)
            num_list.append(str_num)
        number //= base_n

    # 마지막에 몫을 추가할 때도
    if number < 10:
        num_list.append(str(number % base_n))

    else:
        plus_number = number - 10
        str_num = chr(ord('A') + plus_number)
        num_list.append(str_num)

    num_list.reverse()
    return num_list

def solution(n, t, m, p):
    total_num = []
    # 먼저 n진수로 쭉 수를 늘여놓은 다음에 mk+p배수에 있는 걸 솎아내는 식으로
    for i in range(0, t*m):
        total_num.extend(decimal_to_base_n(i,n))

    # 나누는 수와 나머지가 같을 순 없으므로
    if p == m:
        p -= m
    answer = [str_num for idx, str_num in enumerate(total_num) if (idx+1) % m == p]
    answer = answer[:t]
    return ''.join(answer)

if __name__ == '__main__':
    print(solution(16,16,2,2))