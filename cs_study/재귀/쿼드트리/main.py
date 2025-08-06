def dfs(r, c, N, results, maps):
    change_flag = False
    past = maps[r][c]
    for i in range(N):
        for j in range(N):
            if past != maps[r+i][c+j]:
                change_flag = True
                break

    if not change_flag:
        results.append((past, N))
        return

    # 왼쪽 위부터 Z방향으로 오른쪽 아래까지
    dfs(r, c, N // 2, results, maps)
    dfs(r, c + N // 2, N // 2, results, maps)
    dfs(r + N // 2, c, N // 2, results, maps)
    dfs(r + N // 2, c + N // 2, N // 2, results, maps)

def solution(maps, N):
    results = []
    dfs(0, 0, N, results, maps)

    # results 풀어서 ()안으로 담기
    answer = ''
    compare_depth = N
    for idx, (num, depth) in enumerate(results):
        while compare_depth > depth:
            answer += "("
            compare_depth //= 2
        while compare_depth < depth:
            answer += ")"
            compare_depth *= 2
        answer += str(num)

        # 다음 블록이 더 큰 depth면, 지금까지 열린 괄호 닫기
        if idx+1 < len(results):
            next_depth = results[idx+1][1]
            if next_depth > depth:
                while compare_depth < next_depth:
                    answer += ")"
                    compare_depth *= 2

    # 마지막 나올 때 덮기
    while compare_depth < N:
        answer += ")"
        compare_depth *= 2
    return answer

if __name__ == "__main__":
    N = int(input())
    maps = []
    for _ in range(N):
        line = input()
        maps.append(list(map(int, line)))
    print(solution(maps, N))