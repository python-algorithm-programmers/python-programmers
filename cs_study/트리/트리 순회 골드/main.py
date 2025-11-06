"""
루트 노드가 어디서부터 시작되는 건지를 알아야함
"""
import sys
sys.setrecursionlimit(10**7)

def dfs(cur_node, visited, total_cnt):
    visited[cur_node] = True
    if all(visit for visit in visited):
        return

    total_cnt[0] += 1
    if cur_node == 0:
        return

    left, right = adj_dict[cur_node]

    dfs(left, visited, total_cnt)
    if all(visit for visit in visited):
        return
    total_cnt[0] += 1

    dfs(right, visited, total_cnt)
    if all(visit for visit in visited):
        return
    total_cnt[0] += 1


def solution(N, adj_dict):
    # 루트 노드 찾을 때는 set으로 찾기
    all_node = set(range(1, N+1))
    child_node = set()
    for parent in all_node:
        for child in adj_dict[parent]:
            child_node.add(child)

    root_node = list(all_node - child_node)
    root = root_node[0]

    visited = [False] * (N+1)
    visited[0] = True
    total_cnt = [0]
    dfs(root, visited, total_cnt)
    return total_cnt[0]

if __name__ == "__main__":
    N = int(input())
    adj_dict = {}
    for _ in range(N):
        parent, child1, child2 = map(int, input().split())
        if child1 != -1 and child2 != -1:
            adj_dict[parent] = (child1, child2)

        else:
            if child1 == -1 and child2 == -1:
                adj_dict[parent] = (0, 0)

            elif child1 == -1:
                adj_dict[parent] = (0, child2)

            elif child2 == -1:
                adj_dict[parent] = (child1, 0)

    print(solution(N, adj_dict))
