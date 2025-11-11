# def query_min(left, right, idx, q_s, q_e):
#     if q_s < left or right < q_e:
#         return -1
#
#     if
#
#     if left == right:
#         return left
#
#     mid = (left + right) // 2
#     result = query_min(left, mid, idx*2, q_s, q_e)
#     if result != -1:
#         return result
#     return query_min(mid+1, right, idx*2+1, q_s, q_e)
#
# def seg_max_update(left, right, idx, target, new_val):
#     if left == right:
#         segment_max_tree[idx] = new_val
#         maps[target] = new_val
#         return segment_max_tree[idx]
#
#     mid = (left + right) // 2
#     if target <= mid:
#         seg_max_update(left, mid-1, idx*2, target, new_val)
#     else:
#         seg_max_update(mid+1, right, idx*2+1, target, new_val)
#
#     segment_max_tree[idx] = max(
#         segment_max_tree[idx*2], segment_max_tree[idx*2+1]
#     )
#     return segment_max_tree[idx]
#
# def seg_min_update(left, right, idx, target, new_val):
#     if left == right:
#         segment_min_tree[idx] = new_val
#         maps[target] = new_val
#         return segment_min_tree[idx]
#
#     mid = (left + right) // 2
#     if target <= mid:
#         seg_min_update(left, mid-1, idx*2, target, new_val)
#     else:
#         seg_min_update(mid+1, right, idx*2+1, target, new_val)
#
#     segment_min_tree[idx] = min(
#         segment_min_tree[idx * 2], segment_min_tree[idx * 2 + 1]
#     )
#     return segment_min_tree[idx]
#
# if __name__ == "__main__":
#     import sys
#     from math import ceil, log
#     input = sys.stdin.readline
#
#     N = int(input())
#     for _ in range(N):
#         T = int(input())
#         H = ceil(log(T, 2)) + 1
#         tree_size = 2**(H+1) - 1
#         segment_min_tree = [0] * tree_size
#         segment_max_tree = [0] * tree_size
#
#         maps = []
#         for _ in range(T):
#             cmd, input_data = input().split()
#             input_data = int(input_data)
#             if cmd == "I":
#                 maps.append(input_data)
#                 seg_min_update(0, len(maps)-1, 1, len(maps)-1, input_data)
#                 seg_max_update(0, len(maps)-1, 1, len(maps)-1, input_data)
#             else:
#                 if input_data == -1:
#                     min_data = segment_min_tree[1]
#                     seg_min_update(0, len(maps)-1, 1, len(maps)-1, input_data)
#
#                 else:
#                     max_data = segment_max_tree[1]
#
#
#
#
#
#
#
