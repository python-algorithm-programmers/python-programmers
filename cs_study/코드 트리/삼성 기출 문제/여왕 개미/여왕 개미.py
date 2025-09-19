

if __name__ == "__main__":
    import heapq
    ant_diff_heap = []
    ant_heap = []
    N = int(input())
    for _ in range(N):
        command_list = list(map(int, input().strip().split()))
        command = command_list[0]

        if command == 100:
            ant_heap.extend(command_list[2:])
            heapq.heapify(ant_heap)

            # 크기 비교가 되서 튜플로 묶기
            # 힙은 거리값이 젤 큰걸 앞으로 오게 하는
            # (-diff, num, index-1 꼴)
            for i in range(len(ant_heap)):
                if i == 0:
                    heapq.heappush(ant_diff_heap, (0, ant_heap[i], i))
                    continue

                diff = ant_heap[i] - ant_heap[i - 1]
                heapq.heappush(ant_diff_heap, (-diff, ant_heap[i], i))

        elif command == 200:
            ant_house = command_list[1]
            # heap도 넣고 queue에도 넣고 해야됨
            heapq.heappush(ant_heap, ant_house)

            # 차이 갱신해서 다시 넣기
            ant_diff_heap.clear()
            for i in range(len(ant_heap)):
                if i == 0:
                    heapq.heappush(ant_diff_heap, (0, ant_heap[i], i))
                    continue

                diff = ant_heap[i] - ant_heap[i - 1]
                heapq.heappush(ant_diff_heap, (-diff, ant_heap[i], i))

        elif command == 300:
            index = command_list[1]

            # queue에서 빼기
            ant_heap.pop(index-1)

            # 차이 갱신해서 다시 넣기
            ant_diff_heap.clear()
            for i in range(len(ant_heap)):
                if i == 0:
                    heapq.heappush(ant_diff_heap, (0, ant_heap[i], i))
                    continue

                diff = ant_heap[i] - ant_heap[i - 1]
                heapq.heappush(ant_diff_heap, (-diff, ant_heap[i], i))

        else:
            ant_cnt = command_list[1]
            if ant_cnt == 1:
                print(-1*sum(ab[0] for ab in ant_diff_heap))
            else:
                # 마지막 1개 빼고, 거리가 긴순으로 시작 점을 정하기
                start_list = []
                time_list = []
                for i in range(ant_cnt-1):
                    minus_diff, num, index = ant_diff_heap[i]
                    start_list.append(index)

                # 시작점은 하나 넣어 주기
                start_list.append(0)
                heapq.heapify(start_list)

                # 역순으로 탐색해서 시간 타임 비교
                past_index = 0
                for i in range(len(start_list)-1, -1, -1):
                    # 다음 인덱스가 없는 시작점이면 생략
                    if start_list[i] + 1 == len(ant_heap):
                        past_index = start_list[i]
                        continue

                    time = 0
                    # 끝점인 경우
                    if past_index == 0:
                        for j in range(start_list[i], len(ant_heap)-1):
                            time_diff = ant_heap[j+1] - ant_heap[j]
                            time += time_diff

                        time_list.append(time)
                        past_index = start_list[i]

                    # 이전 인덱스가 존재하는 경우
                    else:
                        for j in range(start_list[i], past_index-1):
                            time_diff = ant_heap[j + 1] - ant_heap[j]
                            time += time_diff

                        time_list.append(time)
                        past_index = start_list[i]

                time_list.sort()
                print(time_list[-1])


