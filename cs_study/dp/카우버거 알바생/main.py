def solution(N, M, K, orders):
    dp = [[0]*(N+1) for _ in range(N+1)]
    for cheeze, potato in orders:


    return max(dp)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    orders = []
    for _ in range(N):
        orders.append(list(map(int, input().split())))
    print(solution(N, M, K, orders))