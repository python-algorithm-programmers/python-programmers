
def perm():
    def dfs(depth):
        if depth == M:
            result.append(path[:])
            return

        for i in range(N):
            if not visited[i]:
                visited[i] = True
                path.append(nums[i])
                dfs(depth+1)
                path.pop()
                visited[i] = False

    nums = [1, 2, 3, 4]
    N = len(nums)
    M = 3
    visited = [False] * N
    path = []
    result = []
    dfs(0)
    return result


def comb():
    def dfs(idx, depth):
        if depth == M:
            result.append(path[:])
            return

        if idx == N:
            return

        # depth는 선택 수를 의미
        # 아래는 선택 안하고 다음 것으로 선택햇다는 것을 의미
        dfs(idx+1, depth)
        path.append(nums[idx])
        dfs(idx+1, depth + 1)
        path.pop()

    nums = [1, 2, 3, 4]
    N = len(nums)
    M = 3
    path = []
    result = []
    dfs(0, 0)
    return result

print(perm())
print(comb())