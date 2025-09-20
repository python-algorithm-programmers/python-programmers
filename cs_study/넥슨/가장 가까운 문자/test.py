def solution(queries, s):
    # 글자 인덱스 딕셔너리로 설정해두기
    char_dict = {}
    for i, char in enumerate(s):
        char_dict.setdefault(char, []).append(i)

    answer = []
    # 가장 가까운 인덱스 앞, 뒤나 둘 중 하나를 선별
    for query in queries:
        idx_list = char_dict[s[query]]

        # 이분 탐색으로 특정 인덱스보다 바로 왼쪽에 있는 인덱스로 조사
        idx = bisect.bisect_left(idx_list, query)
        targets = []

        # 앞에 다른 인덱스가 있다
        if idx > 0:
            targets.append(idx_list[idx-1])

        # 뒤에 다른 인덱스가 있다
        if idx < len(idx_list) - 1:
            targets.append(idx_list[idx+1])

        if not targets:
            answer.append(-1)

        targets.sort(key=lambda x: (abs(x-query), x))
        answer.append(targets[0])
    return answer



if __name__ == "__main__":
    import bisect
    queries = [0]
    s = "baabb"
    print(solution(queries, s))