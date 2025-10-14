
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def dfs_sort(arr):
    if len(arr) == 1:
        return arr

    # 이분탐색 적용
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sort = dfs_sort(left)
    right_sort = dfs_sort(right)
    return merge(left_sort, right_sort)





if __name__ == "__main__":
    arr = [5,4,1,3,8, 150, 120, 135]
    print(dfs_sort(arr))