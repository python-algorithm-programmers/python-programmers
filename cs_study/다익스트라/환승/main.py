import heapq
from collections import deque
def solution(N, K, M, adj_dict):
    INF = -1
    dist = [INF] * (N+M+1)
    queue = deque([1])
    dist[1] = 1
    while queue:
        cur = queue.popleft()
        if cur == N:
            return dist[cur]

        for nxt in adj_dict.get(cur, []):
            if dist[nxt] == INF:
                # 튜브 지날때는 거리 증가 안하므로 현재 누적 거리로
                if nxt > N:
                    dist[nxt] = dist[cur]

                else:
                    dist[nxt] = dist[cur] + 1
                queue.append(nxt)

    return -1

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N, K, M = map(int, input().split())
    adj_dict = {}
    tube_id = N

    for _ in range(M):
        station_list = list(map(int, input().split()))
        tube_id += 1
        adj_dict[tube_id] = station_list
        for i in range(K):
            adj_dict.setdefault(station_list[i], []).append(tube_id)

    print(solution(N, K, M, adj_dict))