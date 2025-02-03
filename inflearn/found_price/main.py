from collections import deque
def solution(prices):
   queue = deque(prices)
   result = []
   while queue:
       test_things = queue.popleft()
       cnt = 0
       for content in queue:
           cnt += 1
           if test_things > content:
               break

       result.append(cnt)
   return result


if __name__ == "__main__":
    import sys
    prices = list(map(int, sys.stdin.readline().strip()[1:-1].split(", ")))
    print(solution(prices))
