def solution(n):
    # n의 이진수에서 1의 개수를 셈
    count_ones = bin(n).count('1')

    # n보다 큰 수를 순차적으로 확인하면서 1의 개수가 같은 수를 찾음
    while True:
        n += 1
        if bin(n).count('1') == count_ones:
            return n


if __name__ == '__main__':
    print(solution(15))