def build_segment(left, right, idx):
    if left == right:
        segment_tree[idx] = nums[left]
        return segment_tree[idx]

    # 이분 탐색을 재귀로 적용
    mid = (left + right) // 2
    segment_tree[idx] = build_segment(left, mid, idx*2) + build_segment(mid+1, right, idx*2+1)
    return segment_tree[idx]

def update(left, right, idx, target, change_val):
    if left == right:
        nums[left] = change_val
        segment_tree[idx] = change_val
        return segment_tree[idx]

    mid = (left + right) // 2
    if target <= mid:
        update(left, mid, idx*2, target, change_val)
    else:
        update(mid+1, right, idx*2+1, target, change_val)

    segment_tree[idx] = segment_tree[idx*2] + segment_tree[idx*2+1]
    return segment_tree[idx]

def find(left, right, idx, query_left, query_right):
    if right < query_left or left > query_right:
        return -1

    if segment_tree[idx] == 0:
        return -1

    if left == right:
        return left

    mid = (left + right) // 2
    result = find(left, mid, idx*2, query_left, query_right)
    if result != -1:
        return result

    return find(mid+1, right, idx*2 + 1, query_left, query_right)


if __name__ == "__main__":
    import sys
    from math import ceil, log
    sys.setrecursionlimit(10**7)

    input = sys.stdin.readline
    N, Q = map(int, input().split())
    nums = list(map(int, input().split()))
    H = ceil(log(len(nums),2)) + 1
    tree_size = pow(2, H+1) - 1
    segment_tree = [0] * tree_size
    move_loc = 0

    # 세그먼트 트리 생성
    build_segment(0, N-1, 1)

    for _ in range(Q):
        cmd_list = list(map(int, input().split()))
        command = cmd_list[0]
        left, right = 0, N-1
        # 명소 지정 해제, 토글 방식으로 해제
        if command == 1:
            sights = cmd_list[1]
            new_val = 1 - nums[sights-1]
            update(left, right, 1, sights-1, new_val)

        # 시계방향 이동
        elif command == 2:
            move_loc = (move_loc + cmd_list[1]) % N

        # 최소 몇 칸 움직이는 지확인
        else:
            # 시계 방향이므로 최대한 오른쪽에서 탐색해야 덜 이동
            where = find(0, N-1, 1, move_loc, N-1)
            if where != -1:
                print(where - move_loc)
                continue

            where = find(0, N-1, 1, 0, move_loc-1)
            if where == -1:
                print(-1)
            else:
                print(N - (move_loc - where))