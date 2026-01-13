def solution(numbers):
    if numbers[0][0] == 0:
        return "W"

    answer_str = ""
    # 적분하기
    for const, coeff in numbers:
        coeff += 1
        const //= (coeff)
        #print(const)

        # 계수부터 넣기
        if abs(const) != 1:
            # 계수의 음양에 따라 다르게 적용
            if const < 0:
                answer_str += str(const)
            else:
                # 첫 시작이면 + 배제
                if answer_str == "":
                    answer_str += str(const)
                else:
                    answer_str += "+"
                    answer_str += str(const)
        else:
            if const == -1:
                answer_str += "-"
            else:
                if answer_str != "":
                    answer_str += "+"

        # 계수만큼 x넣기
        for _ in range(coeff):
            answer_str += "x"

    # 상수 붙이기
    answer_str += "+W"
    return answer_str

if __name__ == "__main__":
    input_str = input().strip()
    numbers = []

    # 항 구분
    # 계수가 -일 때 구분이 되지 않음
    const = ""
    coeff = 0
    plus_flag = 1
    for char in input_str:
        if char == "+" or char == "-":
            if char == "+":
                final = int(const) * plus_flag
                numbers.append((final, coeff))
                plus_flag = 1
                const = ""
                coeff = 0
            else:
                if const != "":
                    final = int(const) * plus_flag
                    numbers.append((final , coeff))
                    const = ""
                    coeff = 0
                plus_flag = -1

        elif char == "x":
            coeff += 1

        else:
            const += char

    # 마지막에 상수 넣어주기
    numbers.append((int(const) * plus_flag, coeff))
    print(solution(numbers))
