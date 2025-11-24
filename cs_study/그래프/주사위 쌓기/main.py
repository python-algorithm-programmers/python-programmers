def solution(N, adj_dict):
    answer = 0

    # 맨처음, 첫 주사위에 6가지 중 어느 것으로 시작할 지 선택
    for i in range(1, 7):
        max_num = 0
        next_num = 0

        # 주사위 수만큼 탐색
        for j in range(1, N+1):
            # 선택된 숫자부터 아래에 주사위에서 이어 나가기
            if next_num == 0:
                next_num = i

            # 리스트에서 배제
            out_list = [j for j in range(1, 7)]
            a = adj_dict[j][next_num]
            out_list.remove(next_num)
            out_list.remove(a)

            # 다음 주사위 윗면 갱신
            next_num = a

            # 최댓값 찾고 더하기
            max_num += max(out_list)

        answer = max(answer, max_num)
    return answer

if __name__ == "__main__":
    N = int(input())
    adj_dict = {i: {} for i in range(1, N+1)}
    for i in range(1, N+1):
        A, B, C, D, E, F = map(int, input().split())
        adj_dict[i][A] = F
        adj_dict[i][F] = A

        adj_dict[i][B] = D
        adj_dict[i][D] = B

        adj_dict[i][C] = E
        adj_dict[i][E] = C

    #print(adj_dict)
    print(solution(N, adj_dict))

