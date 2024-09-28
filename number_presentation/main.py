def find_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def find_max_numbers(n):
    max_number = 0
    for i in range(1, n+1):
        max_number += i
        if max_number > n:
            return i


def solution(n):
    answer = 1
    for i in range(2, n+1):
        # 종료 조건
        if n < find_sum(i):
            break

        # 홀수 일때
        if i % 2 == 1:
            if n % i == 0:
                answer += 1
        else:
          if n % i == i//2:
            answer += 1

    return answer

if __name__ == '__main__':
    print(solution(15))
