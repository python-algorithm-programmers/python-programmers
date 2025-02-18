def solution(W, beg_list):
    beg_list.sort(key=lambda x:x[1], reverse=True)
    remainder = W
    result = 0

    while remainder > 0:
        for weight, per_price in beg_list:
            # 더 큰 지 확인
            if remainder >= weight:
                remainder -= weight
                result += (weight * per_price)

            else:
                result += (remainder * per_price)
                remainder = 0
                break

    return result


if __name__ == "__main__":
    import sys
    input_list = list(map(int, sys.stdin.readline().strip().split(" ")))
    W, N = input_list[0], input_list[1]

    beg_list = []
    for __ in range(N):
        weight_list = list(map(int, sys.stdin.readline().strip().split(" ")))
        beg_list.append((weight_list[0], weight_list[1]))

    print(solution(W, beg_list))