def build_tree(left, right, idx, input_list, segment_tree):
    if left == right:
        segment_tree[idx] = input_list[left]
        return segment_tree[idx]

    mid = (left + right) // 2
    segment_tree[idx] = min(
        build_tree(left, mid, idx*2, input_list, segment_tree),
        build_tree(mid+1, right, idx * 2 + 1, input_list, segment_tree)
    )

    return segment_tree[idx]

def find(left, right, idx, q_left, q_right, segment_tree):
    if q_right < left or right < q_left:
        return float("inf")

    # 더 이상 자식 노드까지 탐색할 필요없이 최솟값인 부모 노드 반영
    if q_left <= left and right <= q_right:
        return segment_tree[idx]

    # 나머지 범위에 대한 조사 = 일부만 겹치는 경우
    mid = (left+right) // 2
    left_min = find(left, mid, idx*2, q_left, q_right, segment_tree)
    right_min = find(mid+1, right, idx*2+1, q_left, q_right, segment_tree)
    return min(left_min, right_min)

def solution(N, input_list, test_case):
    H = ceil(log(N, 2)) + 1
    tree_size = pow(2, H+1) - 1
    segment_tree = [0] * tree_size
    build_tree(0, N-1, 1, input_list, segment_tree)
    for a, b in test_case:
        print(find(0, N-1, 1, a-1, b-1, segment_tree))


if __name__ == "__main__":
    import sys
    from math import ceil, log
    input = sys.stdin.readline
    N, M = map(int, input().split())
    input_list = []
    for _ in range(N):
        input_list.append(int(input()))

    test_case = []
    for _ in range(M):
        a, b = map(int, input().split())
        test_case.append((a, b))

    solution(N, input_list, test_case)

