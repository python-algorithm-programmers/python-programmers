def combi(i, j, size_p, size_m, plus_list, minus_list, result, final):
    if i == size_p and j == size_m:
        final.append(result[:])
        return

    if j < size_m:
        result.append(minus_list[j])
        combi(i, j+1, size_p, size_m, plus_list, minus_list, result, final)
        result.pop()

    if i < size_p:
        result.append(plus_list[i])
        combi(i+1, j, size_p, size_m, plus_list, minus_list, result, final)
        result.pop()

def calculate(perm_list, K):
    cur = 0
    for input_data in perm_list:
        if input_data > 0:
            cur += input_data

        else:
            if cur >= 0:
                if cur % K == 0:
                    cur += input_data
                else:
                    cur -= (cur % K)
            else:
                cur += input_data

    return cur


def solution(N, M, plus_list, minus_list, K):
    result = []
    final = []
    new_minus_list = []
    # 마이너스 리스트 추가 시, minus 붙여서
    for minus_input in minus_list:
        new_minus_list.append(-minus_input)

    # 순열로 조합 찾기
    combi(0, 0, len(plus_list), len(minus_list), plus_list, new_minus_list, result, final)

    # 조합별로 값 계산
    candidates = []
    #print(final)
    for perm_list in final:
        cal_data = calculate(perm_list, K)
        candidates.append(cal_data)

    candidates.sort(reverse=True)
    #print(candidates)

    test_list = [27, -44, 51, -62, -7, -16]
    #print("test", calculate(test_list, K))

    return candidates[0]


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    N = int(input())
    plus_list = list(map(int, input().split()))

    M = int(input())
    minus_list = list(map(int, input().split()))
    K = int(input())
    print(solution(N, M, plus_list, minus_list, K))

