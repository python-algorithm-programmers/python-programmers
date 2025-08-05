import heapq
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    heap_queue = []
    for _ in range(N):
        num = int(input())
        if num != 0:
            heapq.heappush(heap_queue, (abs(num), num))

        else:
            if not heap_queue:
                print(0)
            else:
                print(heapq.heappop(heap_queue)[1])