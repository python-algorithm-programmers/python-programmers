from functools import reduce
def get_divisors(n):
    divisor_list = []
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            if j == n:
                divisor_list.append(i)

    # 끝에서 좁혀가면서 tuple 만들기
    total_cnt = len(divisor_list)

    # 짝수인 경우
    if total_cnt % 2 == 0:
        divisor_tuple_list = [[divisor_list[i], divisor_list[total_cnt-1-i]] for i in range(total_cnt) if divisor_list[i] >= divisor_list[total_cnt-1-i] and divisor_list[i] >= 3]

    else:
        medium = total_cnt // 2
        insert_num = divisor_list[medium]
        divisor_list.insert(medium, insert_num)
        divisor_tuple_list = [[divisor_list[i], divisor_list[total_cnt-1-i]] for i in range(total_cnt) if divisor_list[i] >= divisor_list[total_cnt-1-i] and divisor_list[i] >= 3]

    return divisor_tuple_list

def solution(brown, yellow):
    total = brown + yellow
    divisor_tuple_list = get_divisors(total)

    for divisor_tuple in divisor_tuple_list:
        if ((divisor_tuple[0]-2) *(divisor_tuple[1]-2)) == yellow:
            return divisor_tuple

    return divisor_tuple_list

if __name__ == "__main__":
    brown = 10
    yellow = 2
    print(solution(brown, yellow))