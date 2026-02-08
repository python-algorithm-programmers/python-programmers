def solution(N, M, K, orders):
    orders.sort(key=lambda x:(x[0], x[1]))

    # 현재 사용한 치즈버거, 감자 튀김 기반 기준 최대 주문 수
   # 현재 사용한 치즈버거, 감자 튀김 -> 최대 주문수
    dp = {
        (0, 0): 0
    }
    for cheese, potato in orders:
        next_dp = dict(dp)
        #print(cheese, potato)
        #print("before next_dp")
        #print(next_dp)

        for (c, p), order_cnt in dp.items():
            next_c, next_p = c+cheese, p+potato
            if next_c <= M and next_p <= K:
                next_dp[(next_c, next_p)] = max(
                    next_dp.get((next_c, next_p), 0),
                    order_cnt + 1
                )
        dp = next_dp
        #print("next next_dp")
        #print(next_dp)
        #print()

    return max(dp.values())

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    orders = []
    for _ in range(N):
        orders.append(list(map(int, input().split())))
    print(solution(N, M, K, orders))