def dfs(i, j, plus, minus, path, result):
    # i: plus index
    # j: minus index

    # 모든 plus와 minus를 다 넣었다면 종료
    if i == len(plus) and j == len(minus):
        result.append(path[:])
        return

    # minus_list 요소를 넣는 선택지
    if j < len(minus):
        path.append(minus[j])
        dfs(i, j+1, plus, minus, path, result)
        path.pop()

    # plus_list 요소를 넣는 선택지
    if i < len(plus):
        path.append(plus[i])
        dfs(i+1, j, plus, minus, path, result)
        path.pop()


def interleave(plus_list, minus_list):
    result = []
    dfs(0, 0, plus_list, minus_list, [], result)
    return result


plus = [50, 30, 70, 90]
minus = [100, 100]

res = interleave(plus, minus)
for r in res:
    print(r)