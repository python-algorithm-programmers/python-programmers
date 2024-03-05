def dfs(numbers, target, total):
    # 종료 조건
    if not numbers:
        if total == target:
            return 1

        else:
            return 0

    number = numbers[0]
    next_numbers = numbers[1:]
    return (dfs(next_numbers, target, total+number)
            + dfs(next_numbers, target, total-number))

def solution(numbers, target):
    return dfs(numbers, target, 0)

if __name__ == '__main__':
    print(solution([4, 1, 2, 1],4))