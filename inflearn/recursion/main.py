def factorial(number):
    # 종료 조건
    if number == 1:
        return 1

    # 줄여 나가는 조건
    return number * factorial(number-1)

# 재귀함수는 문제의 범위를 조금씩 좁혀나가는 것이 포인트
def is_palindrome(string):
    n = len(string)
    print(string)
    # 종료 조건
    if n == 0:
        return True

    # 줄여 나가는 조건
    if string[0] != string[n-1]:
        return False

    return is_palindrome(string[1:n-1])


if __name__ == "__main__":
    #print(factorial(4))
    import sys
    sys.stdin = open('input.txt')
    string = input()
    print(is_palindrome(string))