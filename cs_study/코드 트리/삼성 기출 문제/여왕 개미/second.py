def dfs(idx, cnt, combi, combi_total, ant_cnt, len_diff, go_away):
    if cnt == ant_cnt - 1:
        combi_total.append(combi[:])
        return

    if idx == len_diff:
        return

    dfs(idx+1, cnt, combi, combi_total, ant_cnt, len_diff, go_away)

    if idx not in go_away:
        combi.append(idx)
        dfs(idx+1, cnt+1, combi, combi_total, ant_cnt, len_diff, go_away)
        combi.pop()

if __name__ == "__main__":
    import heapq
    ant_heap = []
    N = int(input())
    for _ in range(N):
        command_list = list(map(int, input().strip().split()))
        command = command_list[0]

        if command == 100:
            past = 0
            for ant_home in command_list[2:]:
                if past == 0:
                    ant_heap.append([ant_home, True, 0])

                else:
                    diff = ant_home - past
                    ant_heap.append([ant_home, True, diff])

                past = ant_home
            heapq.heapify(ant_heap)

        elif command == 200:
            ant_house = command_list[1]
            # heap도 넣고 인덱스 파악
            heapq.heappush(ant_heap, [ant_house,True,0])
            ant_idx = ant_heap.index([ant_house,True,0])

            # 차이 배열에도 해당 인덱스에 차이값 넣어주기
            for i in range(ant_idx-1, -1 ,-1):
                if ant_heap[i][1]:
                    diff = ant_heap[ant_idx][0] - ant_heap[i][0]
                    ant_heap[ant_idx][2] = diff
                    break

        elif command == 300:
            index = command_list[1]

            # 비활성화
            ant_heap[index-1][1] = False

            # 그 이전이나 이후의 활성화된 첫번째 값을 0으로 만듦
            for i in range(len(ant_heap)):
                if ant_heap[i][1]:
                    ant_heap[i][2] = 0
                    break

            if index == len(ant_heap):
                ant_heap[index - 1][2] = 0

            # 차이값 갱신
            else:
                # 그 다음 활성화된 인덱스 찾고
                update_index = 0
                for i in range(index, len(ant_heap)):
                    if ant_heap[i][1]:
                        update_index = i
                        break

                # 찾은 다음 활성화된 이전 인덱스와의 차이값으로 갱신해야됨
                for j in range(index-2, -1, -1):
                    if ant_heap[j][1]:
                        diff = ant_heap[update_index][0] - ant_heap[j][0]
                        ant_heap[update_index][2] = diff
                        break

        else:
            ant_cnt = command_list[1]
            if ant_cnt == 1:
                print(sum(ant_h[2] for ant_h in ant_heap if ant_h[1]))

            else:
                # 조합
                len_diff = len(ant_heap)
                combi, combi_total = [], []
                go_away = [i for i in range(len(ant_heap)) if not ant_heap[i][1]]
                dfs(1, 0, combi, combi_total, ant_cnt, len_diff, go_away)

                # -1로 구분지어 구간 나누기
                best_time = 10**10
                for combi_sel in combi_total:
                    new_ant_heap = [ant_h[:] for ant_h in ant_heap]
                    time_spent, total_time = 0, 0
                    for combi_idx in combi_sel:
                        new_ant_heap[combi_idx][2] = -1

                    # 탐색
                    for i in range(1, len_diff):
                        if new_ant_heap[i][2] == -1 and new_ant_heap[i][1]:
                            total_time = max(total_time, time_spent)
                            time_spent = 0

                        elif new_ant_heap[i][2] != -1 and new_ant_heap[i][1]:
                            time_spent += new_ant_heap[i][2]

                    # 마지막 잔반 처리
                    total_time = max(total_time, time_spent)
                    best_time = min(total_time, best_time)


                print(best_time)
