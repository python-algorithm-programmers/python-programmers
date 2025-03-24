from functools import cmp_to_key


def compare(a,b):
    if a+b > b+a:
        return -1
    elif a+b == b+a:
        return 0
    else:
        return 1

def solution(numbers):
    # 숫자를 문자열로 변환
    numbers_str = list(map(str, numbers))

    # 사용자 정의 비교 함수로 정렬
    sorted_numbers = sorted(numbers_str, key=cmp_to_key(compare))

    # 0으로 시작한다면 전부 0이라는 뜻
    if sorted_numbers[0] == "0":
        return "0"

    # 결과 이어붙이기
    return ''.join(sorted_numbers)

if __name__ == "__main__":
    numbers = [12, 1213]
    print(solution(numbers))