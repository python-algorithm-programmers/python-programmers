g_result = 0
g_numbers = []
g_target = 0

def recursion(index, cur_sum):
    global g_result, g_numbers, g_target

    # 종료 조건
    # 모든 숫자를 다 사용한 경우
    if index == len(g_numbers):
        # 결과값이 동일R한 경우에만
        if g_target == cur_sum:
            g_result += 1
        return

    # 더하기
    recursion(index+1, cur_sum+g_numbers[index])

    # 빼기
    recursion(index+1, cur_sum-g_numbers[index])

def solution():
    global g_result, g_numbers, g_target
    recursion(0, 0)
    return g_result

if __name__ == "__main__":
    import sys
    sys.stdin = open("input.txt")
    for i in range(2):
        # 1번
        if i == 0:
            str_arr = input()[1:-1]
            g_numbers = list(map(int, str_arr.split(', ')))

        else:
            g_target = int(input())

    print(solution())
    