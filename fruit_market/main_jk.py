def solution(k, m, score):
    sorted_score = sorted(score,reverse=True)
    result = 0
    idx = 0

    # 리스트를 매번 업데이트하는 것이 아닌
    # 인덱스만 바꿔주면서 리스트를 이용하는 형태로 유도
    while idx <= len(sorted_score) - m:
        fruit_box = sorted_score[idx: idx+m]
        min_fruit = min(fruit_box)
        result += min_fruit * m
        idx += m

    return result


if __name__ == '__main__':
    print(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))