def solution(storey):
    # 5보다 크면 반올림하고
    # 5보다 작으면 그냥 계산하는 게 맞다
    # 5이면 다음자리수를 보되, 5이상이면 반올림하도록 한다
    # while문을 써서 한자리씩 계산하고, 계산된 수가 10으로 나눠서 몫이 0이되면 멈추도록
    answer = 0
    while storey > 0:
        digit = storey % 10
        next_digit = (storey // 10) % 10
        if digit > 5:
            answer += 10 - digit
            storey += 10 - digit

        elif digit < 5:
            answer += digit

        else:
            if next_digit >= 5:
                answer += 10 - digit
                storey += 10 - digit
            else:
                answer += digit

        storey //= 10

    return answer

if __name__ == "__main__":
    storey = 14
    print(solution(storey))
