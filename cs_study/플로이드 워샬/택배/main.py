# DP의 bottom up 형태
# 간선이 1개만 있는 경우는 main에서 반영
# 간선이 2개 이상있는 경우는 k 라는 변수를 두어 적용
# 모든 가짓수를 k(1..2..)로 특정 노드별 간선 1개씩 최소치로 추가해가면서 계산
def solution(floyd, n):
    # 자기 자신은 가중치 값을 0으로 적용
    for i in range(n):
        floyd[i][i][1] = 0

    # 전이 폐쇄와 같은 boolean(이어졌다, 안이어졌다)은 while flag 안으로 처리
    # 그러나 플로이드는 차례로 가야한다?
    for k in range(n):
        for y in range(n):
            if k == y:
                continue
            for x in range(n):
                if y == k or x == k:
                    continue

                min_distance = floyd[y][k][1] + floyd[k][x][1]
                if min_distance < floyd[y][x][1]:
                    floyd[y][x] = [floyd[y][k][0], min_distance]
    return floyd

if __name__ == "__main__":
    n, m = map(int, input().split())
    floyd = [[[0,10**12] for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        start, end, weight = map(int, input().split())
        floyd[start - 1][end - 1] = [end, weight]
        floyd[end - 1][start - 1] = [start, weight]

    answer = solution(floyd, n)
    for y in range(n):
        result = []
        for x in range(n):
            if y == x:
                result.append("-")
            else:
                result.append(str(answer[y][x][0]))
        print(*result)