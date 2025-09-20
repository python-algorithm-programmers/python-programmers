def solve_dp(ant_heap, ant_cnt):
    # 활성화된 집들의 diff만 뽑아서 배열 생성
    diffs = [ant[2] for ant in ant_heap if ant[1]]

    n = len(diffs)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + diffs[i - 1]

    # dp[i][k] = i번째 집까지 k개 그룹으로 나눴을 때 최소 최대 시간
    INF = 10**15
    dp = [[INF] * (ant_cnt + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for k in range(1, ant_cnt + 1):
            # j는 이전 컷 위치
            for j in range(i):
                cost = prefix[i] - prefix[j]  # j+1 ~ i 구간 합
                dp[i][k] = min(dp[i][k], max(dp[j][k - 1], cost))

    return dp[n][ant_cnt]


if __name__ == "__main__":
    import heapq
    ant_heap = []
    N = int(input())
    for _ in range(N):
        command_list = list(map(int, input().strip().split()))
        command = command_list[0]

        if command == 100:  # 초기 개미 집 등록
            past = 0
            for ant_home in command_list[2:]:
                if past == 0:
                    ant_heap.append([ant_home, True, 0])
                else:
                    diff = ant_home - past
                    ant_heap.append([ant_home, True, diff])
                past = ant_home
            heapq.heapify(ant_heap)

        elif command == 200:  # 새로운 개미 집 추가
            ant_house = command_list[1]
            heapq.heappush(ant_heap, [ant_house, True, 0])
            ant_idx = ant_heap.index([ant_house, True, 0])
            for i in range(ant_idx - 1, -1, -1):
                if ant_heap[i][1]:
                    diff = ant_heap[ant_idx][0] - ant_heap[i][0]
                    ant_heap[ant_idx][2] = diff
                    break

        elif command == 300:  # 특정 개미 집 비활성화
            index = command_list[1]
            ant_heap[index - 1][1] = False

            for i in range(len(ant_heap)):
                if ant_heap[i][1]:
                    ant_heap[i][2] = 0
                    break

            if index == len(ant_heap):
                ant_heap[index - 1][2] = 0
            else:
                update_index = 0
                for i in range(index, len(ant_heap)):
                    if ant_heap[i][1]:
                        update_index = i
                        break
                for j in range(index - 2, -1, -1):
                    if ant_heap[j][1]:
                        diff = ant_heap[update_index][0] - ant_heap[j][0]
                        ant_heap[update_index][2] = diff
                        break

        else:  # 400: 최소 시간 계산
            ant_cnt = command_list[1]
            if ant_cnt == 1:
                print(sum(ant_h[2] for ant_h in ant_heap if ant_h[1]))
            else:
                print(solve_dp(ant_heap, ant_cnt))