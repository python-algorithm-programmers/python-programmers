import sys
def solution(N, S, n_arr):
    cur_sum = start = end = 0
    best = N+1
    while end < len(n_arr):
        if cur_sum > S:
            cur_sum -= n_arr[start]
            start += 1
            continue

        elif cur_sum == S:
            length = end - start
            best = min(length, best)

        cur_sum += n_arr[end]
        end += 1

    if best == N:
        return 0
    return best

if __name__ == "__main__":
    N, S = map(int, input().split())
    n_arr = list(map(int, sys.stdin.readline().strip().split()))
    print(solution(N, S, n_arr))