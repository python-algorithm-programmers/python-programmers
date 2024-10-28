def solution(N, K, coins):
    cnt = 0
    for coin in coins:
        # 종결 조건
        if K == 0:
            break

        # 한방에 해결해야되
        cnt += K // coin
        K = K % coin

    return cnt

if __name__ == "__main__":
    import sys
    lines = sys.stdin.readlines()
    N, K = lines[0].strip().split(" ")
    N, K = int(N), int(K)
    coins = []
    for coin in lines[1:]:
        int_coin = int(coin.strip())
        if K >= int_coin:
            coins.append(int_coin)
        else:
            break
    coins.sort(reverse=True)
    print(solution(N, K, coins))