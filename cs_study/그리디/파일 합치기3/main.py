import heapq
def solution(test_cnt, files):
    for file in files:
        heapq.heapify(file)
        cost = 0
        while len(file) > 1:
            first = heapq.heappop(file)
            second = heapq.heappop(file)
            min_sum = first + second

            # 비용 계산
            cost += min_sum
            heapq.heappush(file, min_sum)

        print(cost)


if __name__ == "__main__":
    test_cnt = int(input())
    files = []
    for _ in range(test_cnt):
        files_cnt = int(input())
        files.append(list(map(int, input().split())))
    solution(test_cnt, files)