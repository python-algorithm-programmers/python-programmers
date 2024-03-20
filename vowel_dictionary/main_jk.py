def solution(word):
    # 가중치 계산
    weight = [781, 156, 31, 6, 1]

    # 알파벳 나열 순서
    sort_dict = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}

    # 가중치 계산 * 순서
    result = 0
    for i,char in enumerate(word):
        result += weight[i] * sort_dict[char]

    return result + len(word)

if __name__ == '__main__':
    print(solution("AAA"))