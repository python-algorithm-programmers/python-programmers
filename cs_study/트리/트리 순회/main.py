def dfs_root(node, result, node_dict):
    if node == ".":
        return
    result.append(node)
    left, right = node_dict[node]
    dfs_root(left, result, node_dict)
    dfs_root(right, result, node_dict)

def dfs_middle(node, result, node_dict):
    if node == ".":
        return
    left, right = node_dict[node]
    dfs_middle(left, result, node_dict)
    result.append(node)
    dfs_middle(right, result, node_dict)

def dfs_back(node, result, node_dict):
    if node == ".":
        return
    left, right = node_dict[node]
    dfs_back(left, result, node_dict)
    dfs_back(right, result, node_dict)
    result.append(node)

def solution(node_dict):
    root_result = []
    left_result = []
    right_result = []
    total_results = []

    # 항상 루트는 A라고 함
    root = 'A'
    dfs_root(root, root_result, node_dict)
    dfs_middle(root, left_result, node_dict)
    dfs_back(root, right_result, node_dict)

    total_results.append(root_result)
    total_results.append(left_result)
    total_results.append(right_result)
    return total_results


if __name__ == "__main__":
    N = int(input())
    node_dict = {}
    for _ in range(N):
        root, left, right = input().split()
        node_dict[root] = (left, right)
    answers = solution(node_dict)

    for answer in answers:
        print("".join(answer))