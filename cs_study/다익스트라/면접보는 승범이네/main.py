def solution(N, M, meeting_loc, total_dict):
    # 다익스트라 이용해서 거리 갱신
    # 2개 다 고려
    #print(total_dict['dist'])
    heap_list = []
    for loc in meeting_loc:
        heap_list.append((0, loc))

    while heap_list:
        cur_dis, cur = heapq.heappop(heap_list)
        if cur_dis > total_dict['dist'][cur]:
            continue
        for nxt, nxt_cost in total_dict['adj'][cur]:
            final_dis = cur_dis + nxt_cost
            if final_dis < total_dict['dist'][nxt]:
                total_dict['dist'][nxt] = final_dis
                heapq.heappush(heap_list, (final_dis, nxt))

    result = sorted(total_dict['dist'].items(), key=lambda x:-x[1])
    print(result[0][0])
    print(result[0][1])


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    import heapq

    N, M, K = map(int, input().split())
    total_dict = {}
    INF = 9999999999
    adj = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        U, V, C = map(int, input().split())
        #adj[U].append((V, C))
        adj[V].append((U, C))
        total_dict['adj'] = adj

    dist = {i: INF for i in range(1, N + 1)}
    total_dict['dist'] = dist

    meeting_loc = list(map(int, input().split()))
    for loc in meeting_loc:
        total_dict['dist'][loc] = 0

    solution(N, M, meeting_loc, total_dict)
