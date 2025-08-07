import heapq
from collections import deque


def solution(N, fusion_cnt, cards):
    heapq.heapify(cards)
    while fusion_cnt > 0:
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)
        min_sum = first + second

        # 뺀 카드 2개 넣기
        heapq.heappush(cards, min_sum)
        heapq.heappush(cards, min_sum)
        fusion_cnt -= 1


    return sum(cards)


if __name__ == "__main__":
    N, fusion_cnt = map(int, input().split())
    cards = list(map(int, input().split()))
    print(solution(N, fusion_cnt, cards))
