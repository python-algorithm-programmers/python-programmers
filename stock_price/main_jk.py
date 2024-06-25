def solution(prices):
    # step1: prices의 인덱스를 저장할 stack을 만들어서, 최종적으로 남는 인덱스들 저장
    # step2: step1에서 남은 인덱스들은 최종까지 유지한 것으로 고려

    # step1: 마지막까지 살아남는 인덱스만을 계산하기 위해 그 전에 끝나는 인덱스들 제외
    stack = []
    answer = [0] * len(prices)

    for i, price in enumerate(prices):
        # 마지막꺼만 확인하는 전제는 이전 while문에서 모두 처리가 완료되었다고 생각
        while stack and prices[stack[-1]] > price:
            last = stack.pop()
            answer[last] = i - last

        stack.append(i)

    # step2: 최후의 인덱스들 계산
    while stack:
        last = stack.pop()

        # 인덱스간 거리로 누적 시간을 계산
        answer[last] = len(prices) - 1 - last

    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 2, 3]))