from collections import deque
def solution(prices):
    queue = deque(prices)
    cnt_list = []
    while queue:
        price = queue.popleft()
        cnt = 0
        for left_price in queue:
            if price > left_price:
                cnt += 1
                break
            else:
                cnt += 1

        cnt_list.append(cnt)
    return cnt_list

if __name__ == "__main__":
    import sys
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))
