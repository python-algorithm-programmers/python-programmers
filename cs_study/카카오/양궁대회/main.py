# 점수 합산
def calculate(info, total):
    answer = []
    for combi in total:
        a_sum, b_sum, mini, target = 0, 0, 11, 0
        for i in range(11):
            if mini > combi[i] and combi[i] > 0:
                mini = 10-i
                target = combi[i]

            if combi[i] > info[i]:
                b_sum += (10 - i)

            else:
                if info[i] > 0:
                    a_sum += (10 - i)

        if b_sum > a_sum:
            diff = b_sum - a_sum
            answer.append((diff, mini, target, combi))

    if not answer:
        return [-1]
    answer.sort(key=lambda x: (-x[0], x[1], -x[2]))
    return answer[0][3]


def dfs(idx, cnt, info, result, total):
    if cnt < 0:
        return

    if idx == 11:
        if cnt == 0:
            total.append(result[:])
        return

    # 0을 포함시킨 건, 못맞추고 넘길 수도 있기 때문
    for i in range(cnt+1):
        result.append(i)
        dfs(idx + 1, cnt - i, info, result, total)
        result.pop()


def solution(n, info):
    total = []
    result = []
    dfs(0, n, info, result, total)
    return calculate(info, total)

if __name__ == "__main__":
    n = 10
    info = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]
    print(solution(n, info))