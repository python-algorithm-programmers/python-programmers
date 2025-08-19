import sys
def solution(N, liquid):
    start, end = 0, len(liquid)-1
    best = 10**9
    while start < end:
        cur_sum = liquid[start] + liquid[end]
        if abs(cur_sum) < abs(best):
            best = cur_sum

        if cur_sum > 0:
            end -= 1

        else:
            start += 1

    return best


if __name__ == "__main__":
    N = int(input())
    liquid = list(map(int, sys.stdin.readline().strip().split()))
    print(solution(N, liquid))