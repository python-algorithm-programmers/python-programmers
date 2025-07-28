def dfs(node, parent_node, tree_flag, component_list, visited):
    visited[node] = True
    for next_node in component_list[node]:
        if next_node == parent_node:
            continue

        if visited[next_node]:
            tree_flag[0] = True

        else:
            dfs(next_node, node, tree_flag, component_list, visited)

def solution(component_list, n):
    total_results = 0
    visited = [False] * (n+1)
    for i in range(1, n+1):
        if not visited[i]:
            tree_flag = [False]
            dfs(i, i, tree_flag, component_list, visited)

            if not tree_flag[0]:
                total_results += 1

    return total_results

if __name__ == "__main__":
    turn_cnt = 1
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        component_list = [[] for _ in range(n+1)]
        for _ in range(1, m+1):
            node1, node2 = map(int, input().split())
            component_list[node1].append(node2)
            # 양방향으로 설정하지 않으면,
            # 하나의 트리가 분할되어 계산되는 문제 발생
            component_list[node2].append(node1)
        answer_cnt = solution(component_list, n)

        # switch문 대체
        if answer_cnt == 0:
            print(f"Case {turn_cnt}: No trees.")
        elif answer_cnt == 1:
            print(f"Case {turn_cnt}: There is one tree.")
        else:
            print(f"Case {turn_cnt}: A forest of {answer_cnt} trees.")
        turn_cnt += 1