def solution(N, adj_dict, out_hole, height_data):
    can_escape = [False]*(N+1)
    height_data = [0] + height_data
    queue = deque(out_hole)
    for out in out_hole:
        can_escape[out] = True

    while queue:
        node = queue.popleft()

        # 연관된 것이
        # 고이지도 막히지도 않고 and 높이가 낮은 것
        for nxt in adj_dict[node]:
            if not can_escape[nxt] and height_data[nxt] >= height_data[node]:
                can_escape[nxt] = True
                queue.append(nxt)

    #print(can_escape)
    for i in range(1, N+1):
        if not can_escape[i]:
            return "flood"

    return "no flood"


if __name__ == "__main__":
    import sys
    from collections import deque
    input = sys.stdin.readline

    N, M = map(int, input().split())
    height_data = list(map(int, input().split()))
    adj_dict = {node: [] for node in range(1, N+1)}

    for _ in range(M):
        a, b = map(int, input().split())
        adj_dict[a].append(b)
        adj_dict[b].append(a)

    K = int(input())
    out_hole = list(map(int, input().split()))

    print(solution(N, adj_dict, out_hole, height_data))