def solution(adjacent_metrix, N):
    changed_flag = True
    while changed_flag:
        changed_flag = False
        for y in range(N):
            for x in range(N):
                list_y = adjacent_metrix[y]
                if list_y:
                    if x in list_y:
                        continue
                    for z in range(N):
                        if z in list_y and x in adjacent_metrix[z]:
                            adjacent_metrix[y].append(x)
                            changed_flag = True
                            break

    results = [
        (y+1, len(adjacent_metrix[y]))
        for y in range(N)
    ]
    results.sort(key=lambda x:(-x[1], x[0]))
    max_cnt = results[0][1]
    return [node for node, cnt in results if cnt == max_cnt]


if __name__ == "__main__":
    N, M = map(int, input().split())
    adjacent_metrix = [[] for _ in range(N)]
    for _ in range(M):
        start, end = map(int, input().split())
        adjacent_metrix[end-1].append(start-1)
    answer = solution(adjacent_metrix, N)
    print(*answer)