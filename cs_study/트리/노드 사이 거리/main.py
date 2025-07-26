def solution(node_map, N):
    for k in range(N):
        for y in range(N):
            if y == k:
                continue
            for x in range(N):
                if y == x:
                    node_map[x][x] = 0
                    continue

                if k == y or k == x:
                    continue

                min_distance = node_map[y][k] + node_map[k][x]
                if node_map[y][x] > min_distance:
                    node_map[y][x] = min_distance


if __name__ == "__main__":
    N, M = map(int, input().split())
    qna_list = []
    node_map = [[10001]*N for _ in range(N)]
    for _ in range(N-1):
        start, end, distance = map(int, input().split())
        node_map[start - 1][end - 1] = distance
        node_map[end - 1][start - 1] = distance

    for _ in range(M):
        qna_list.append(list(map(int, input().split())))
    solution(node_map, N)
    for qna in qna_list:
        y, x = qna[0]-1, qna[1]-1
        print(node_map[y][x])
