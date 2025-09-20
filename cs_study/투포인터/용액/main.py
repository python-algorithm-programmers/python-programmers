import sys

def solution(N, line_map):
    start, end = 0, N-1
    best_sum = 2*10**9
    best_couple = []
    while start < end:
        total_sum = line_map[start] + line_map[end]
        if abs(best_sum) >= abs(total_sum):
            best_sum = total_sum
            best_couple = [line_map[start], line_map[end]]

        if total_sum > 0:
            end -= 1
        elif total_sum < 0:
            start += 1
        else:
            return best_couple

    return best_couple

if __name__ == "__main__":
    N = int(input())
    line_map = list(map(int, sys.stdin.readline().strip().split()))
    answer = solution(N, line_map)
    print(*answer)