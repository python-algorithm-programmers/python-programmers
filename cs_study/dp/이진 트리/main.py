def solution(K, node_list):
    node_list = [0, 0] + node_list
    total = 2**(K+1) - 1

    """
    노드 i에서부터 시작해서 아래쪽 리프까지의 최대 경로합
    그래야지 그것에 맞춰 가중치 합 산정이 가능
    가중치는 오직 증가만 가능하므로
    """
    dp = [0] * (total+1)
    result = [0]
    def dfs(idx):
        left = 2 * idx
        right = 2 * idx + 1

        # 리프노드까지 도달하고 로직 시작하도록
        if left > total:
            dp[idx] = node_list[idx]
            return dp[idx]

        # 리프노드까지 찍기
        left_dp = dfs(left)
        right_dp = dfs(right)
        #print(left_dp, right_dp)

        # 좌우 차
        result[0] += abs(left_dp - right_dp)
        #print("result", result)
        dp[idx] = max(left_dp, right_dp) + node_list[idx]
        return dp[idx]

    dfs(1)
    return result[0] + sum(node_list)

if __name__ == "__main__":
    K = int(input())
    node_list = list(map(int, input().split()))
    print(solution(K, node_list))