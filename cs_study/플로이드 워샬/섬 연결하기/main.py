"""
플로이드 워샬 문제
"""
def solution(n, costs):
    adj_list = [[float("inf")]*n for _ in range(n)]
    cost_list = [[0]*n for _ in range(n)]
    for a, b, cost in costs:
        adj_list[a][b] = cost
        adj_list[b][a] = cost

        cost_list[a][b] = cost
        cost_list[b][a] = cost

    for k in range(n):
        for i in range(n):
            if i==k: continue
            for j in range(n):
                if i==j or j==k: continue

                if adj_list[i][k]+adj_list[k][j] < adj_list[i][j]:
                    cost_list[i][j] = 0
                    new_dis = adj_list[i][k]+adj_list[k][j]
                    adj_list[i][j] = new_dis

    #print(cost_list)
    answer = 0
    for a, b, cost in costs:
        if cost_list[a][b] != 0:
            answer += cost

    return answer


