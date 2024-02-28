def solution(clothes):
    cloth_dict = {}
    for cloth in clothes:
        wear, kind = cloth[0], cloth[1]
        cloth_dict.setdefault(kind, []).append(wear)

    # 계산
    answer = 1
    for (k, v) in cloth_dict.items():
        # 종류 별로 없는 경우도 고려해서 +1
        answer *= (len(v)+1)

    # 모두 없는 경우를 제거
    answer -= 1
    return answer

if __name__ == '__main__':
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))