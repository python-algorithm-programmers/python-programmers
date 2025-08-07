from collections import deque

def solution(N, fusion_cnt, cards):
    cards.sort()
    queue = deque(cards)
    while fusion_cnt > 0:
        first = queue.popleft()
        second = queue.popleft()
        min_sum = first + second

        for i in range(N-2):
            if min_sum <= queue[i]:
                queue.insert(i, min_sum)
                queue.insert(i, min_sum)
                break

            # 끝까지 다 온 경우엔 마지막에 삽입
            if i == N-3:
                queue.insert(i+1, min_sum)
                queue.insert(i, min_sum)
                break

        fusion_cnt -= 1

    return sum(queue)







if __name__ == "__main__":
    N, fusion_cnt = map(int, input().split())
    cards = list(map(int, input().split()))
    print(solution(N, fusion_cnt, cards))
