def solution(N, M, num_list):
    max_sum = 0

    # 세 장의 카드를 뽑아 그 합을 구하는 모든 경우의 수를 탐색
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                card_sum = num_list[i] + num_list[j] + num_list[k]

                if card_sum <= M:
                    max_sum = max(max_sum, card_sum)

    return max_sum


if __name__ == '__main__':
    import sys
    lines = sys.stdin.readlines()
    N, M = list(map(int, lines[0].strip().split()))
    num_list = list(map(int, lines[1].strip().split()))
    print(solution(N, M, num_list))