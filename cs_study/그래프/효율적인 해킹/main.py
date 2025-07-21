def solution(adjacent_metrix, N):
    changed_flag = True
    while changed_flag:
        changed_flag = False
        for y in range(N):
            for x in range(N):
                if y == x:
                    continue
                if adjacent_metrix[y][x] == 1:
                    continue
                for z in range(N):
                    if adjacent_metrix[y][z] == 1 and adjacent_metrix[z][x] == 1:
                        adjacent_metrix[y][x] = 1
                        changed_flag = True
                        break

    results = [
        (y+1, sum(adjacent_metrix[y]))
        for y in range(N)
    ]
    results.sort(key=lambda x:(-x[1], x[0]))
    max_cnt = results[0][1]
    return [node for node, cnt in results if cnt == max_cnt]


if __name__ == "__main__":
    N, M = map(int, input().split())
    adjacent_metrix = [[0]*N for _ in range(N)]
    for _ in range(M):
        start, end = map(int, input().split())
        adjacent_metrix[end - 1][start - 1] = 1
    answer = solution(adjacent_metrix, N)
    print(*answer)