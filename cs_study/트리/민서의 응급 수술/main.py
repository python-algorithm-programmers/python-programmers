from collections import deque


def solution(N, adj_dict):
    break_cnt, group_cnt = 0, 0
    visited = [False] * (N+1)
    for start in range(1, N+1):
        if not visited[start]:
            group_cnt += 1
            queue = deque([(start, 0)])
            visited[start] = True

            while queue:
                cur, parent = queue.popleft()
                for nxt in adj_dict[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        queue.append((nxt, cur))
                    # 방문한 곳인 데, 부모가 아니라 이미 큐에 등록된 것
                    # 이러면 두 개의 간선이 있다는 것인데, 사이클을 의미
                    elif nxt != parent:
                        break_cnt += 1

    # 2에서도 사이클 세고, 3에서도 사이클 세므로 나누기 // 2
    break_cnt //= 2
    return group_cnt + break_cnt - 1


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    adj_dict = {
        node: [] for node in range(1, N+1)
    }
    for _ in range(M):
        a, b = map(int, input().split())
        adj_dict[a].append(b)
        adj_dict[b].append(a)

    print(solution(N, adj_dict))