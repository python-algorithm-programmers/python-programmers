def solution(target):
    numbers = [i for i in range(1, 10)]
    cur_min = 0
    cur_max = len(numbers) - 1
    cur_guess = (cur_min + cur_max) // 2

    # while 문으로 찾기
    while cur_min <= cur_max:
        if numbers[cur_guess] == target:
            return True
        elif numbers[cur_guess] < target:
            cur_min = cur_guess + 1
        else:
            cur_max = cur_guess - 1

        cur_guess = (cur_min+cur_max) // 2


if __name__ == "__main__":
    import sys
    sys.stdin = open('input.txt')
    target = int(input())
    print(solution(target))