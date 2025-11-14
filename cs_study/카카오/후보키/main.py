import sys

sys.setrecursionlimit(10 ** 7)


def solution(relation):
    total = []
    result = []
    N = len(relation[0])
    visited = [False] * N

    def dfs(idx, combi):
        if idx == N:
            if combi:
                total.append(combi[:])
            return

        dfs(idx + 1, combi)
        combi.append(idx)
        dfs(idx + 1, combi)
        combi.pop()

    dfs(0, result)
    total.sort(key=lambda x: (len(x), x))
    answer = []
    for find in total:
        # candidate 수만큼 확인
        case = []
        flag = False
        for row in relation:
            sub_case = []
            for key in find:
                sub_case.append(row[key])

            if sub_case in case:
                # print(sub_case)
                flag = True
                break
            case.append(sub_case)

        if flag:
            continue

        # key 하나만 들어간 경우는 빼고
        # 2개 넣는 것을 찾으면 그 이후에 있는 것들은 모두 빼기
        if not answer:
            answer.append(find)
        else:
            can_add = True
            for check in answer:
                if set(check).issubset(set(find)):
                    # print(find)
                    can_add = False
                    break
            if can_add:
                answer.append(find)
        # print(case)
    return len(answer)