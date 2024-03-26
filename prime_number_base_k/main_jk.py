def convert_base_k(n, k):
    # 10진수보다 더 큰수가 나올 수 있음을 고려
    # 자리수를 저장할 변수
    base_num = []
    while n > k:
        if n % k > 9:
            base_num.append(chr(ord('A')+n % k - 10))
        else:
            base_num.append(str(n % k))
        n //= k

    if n % k > 9:
        base_num.append(chr(ord('A') + n - 10))
    else:
        base_num.append(str(n))

    base_num.reverse()
    return ''.join(base_num)

def is_prime_number(n):
    if n == 1:
        return False

    root_num = int(n**0.5)+1
    for i in range(2, root_num):
        if n % i == 0:
            return False

    return True

def solution(n, k):
    # 정답을 담을 리스트
    answer = []

    # k진수 숫자로 변환
    base_k_list = convert_base_k(n,k)

    # 0을 기준으로 split 후에 리스트 반환
    non_zero_list = [x for x in base_k_list.split('0') if x]

    # 반환된 리스트에서 소수가 있는 지 판단
    for non_zero in non_zero_list:
        if is_prime_number(int(non_zero)):
            answer.append(int(non_zero))

    return len(answer)

if __name__ == '__main__':
    print(solution(110011, 10))