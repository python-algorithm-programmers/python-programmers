def solution(toppings):
    answer = 0

    # SET 초기화
    left_set = set()
    right_set = set(toppings)

    # set은 중복이 제거 되므로 원소 갯수를 따로 관리할 딕셔너리가 필요
    left_count, right_count = {}, {}

    # right만 갯수 조사
    for topping in toppings:
        right_count[topping] = right_count.get(topping,0)+1

    # 투포인터 알고리즘 적용
    for topping in toppings:
        left_count[topping] = left_count.get(topping,0)+1
        left_set.add(topping)

        # 오른쪽 꺼는 count를 제거
        right_count[topping] -= 1

        if right_count[topping] == 0:
            right_set.remove(topping)

        # 둘의 사이즈가 똑같으면, 가짓수로 등록
        if len(left_set) == len(right_set):
            answer += 1

    return answer

if __name__ == '__main__':
    print(solution([1, 2, 1, 3, 1, 4, 1, 2]))