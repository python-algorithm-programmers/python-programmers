def solution(want, number, discount):
    # discount에서 want의 물품종류를 모두 갖고 있지 않은 경우는
    # 바로 0을 반환하도록 초기 세팅
    for prd in want:
        if prd not in discount:
            return 0

    answer_dict = {}
    for product, num in zip(want, number):
        answer_dict[product] = num

    start_pt = 0
    check_dict = {}

    # 총 일수
    answer = []

    while True:
        for i in range(start_pt, start_pt+10):
            # 키가 없다면 0을 반환하도록
            current_cnt = check_dict.get(discount[i], 0)

            # 키값의 유무에 관계없이 새로 키값을 만들고 value값을 저장하는 로직
            check_dict[discount[i]] = current_cnt + 1

            # want에 포함된 제품이 아닌 게 discount에 존재하면 break
            if answer_dict.get(discount[i], 0) == 0:
                break

            # 만약에 다른 제품의 갯수가 넘치면 바로 break
            elif check_dict[discount[i]] > answer_dict[discount[i]]:
                break

        if check_dict == answer_dict:
            answer.append(start_pt+1)

        else:
            # dictionary 초기화
            check_dict = {}
            start_pt += 1

            if start_pt > len(discount) - sum(number):
                return len(answer)

if __name__ == '__main__':
    print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))