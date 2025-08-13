def solution(N, K, num_arr):
    start = end = 0
    odd_cnt = 0
    best_even = 0

    while end < N:
        # 홀수인 지 확인해서 카운트 차례로 증가시킴
        if num_arr[end] % 2 == 1:
            odd_cnt += 1

        # 범위안에 홀수가 K보다 많다면 빠질 때까지 반복
        while odd_cnt > K:
            if num_arr[start] % 2 == 1:
                odd_cnt -= 1
            start += 1

        best_even = max(end - start + 1 - odd_cnt, best_even)
        end += 1

    return best_even


if __name__ == "__main__":
    import sys
    N, K = map(int, sys.stdin.readline().strip().split())
    num_arr = list(map(int, sys.stdin.readline().strip().split()))
    print(solution(N, K, num_arr))