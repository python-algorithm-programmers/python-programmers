def _cal(op, first_number, second_number):
    if op == "-":
        result = first_number - second_number
    elif op == "*":
        result = first_number * second_number
    else:
        result = first_number + second_number

    return result

def calculate(final, numbers, operators):
    candidates = []

    # 조합이 나온 것을 먼저 계산하기
    for op_index_combi in final:
        new_numbers = numbers[:]
        new_operators = operators[:]
        #print("start", op_index_combi)
        for op_index in op_index_combi:
            #print(op_index)
            #print(new_operators)

            op = new_operators.pop(op_index)
            first_number = new_numbers.pop(op_index)
            second_number = new_numbers.pop(op_index)
            result = _cal(op, first_number, second_number)
            new_numbers.insert(op_index, result)

        # 나머지 앞에서부터 계산
        #print(new_numbers, new_operators)
        #print("start")
        while new_operators:
            op = new_operators.pop(0)
            first = new_numbers.pop(0)
            second = new_numbers.pop(0)
            result = _cal(op, first, second)

            new_numbers.insert(0, result)
            #print(result)
            #print(new_numbers, new_operators)

        #print("new_numbers", new_numbers[0])
        #print()
        candidates.append(new_numbers[0])

    return candidates

def solution(N, numbers, operators):
    if N == 1:
        return numbers[0]

    result = []
    final = []

    # 조합은 단순 넘어갈 것과 포함할 것을 둠
    M = len(numbers)
    def combi(idx, depth):
        if depth >= M-1:
            if result:
                final.append(result[:])
            return

        combi(idx, depth+1)
        result.append(depth)
        combi(idx+2, depth+2)
        result.pop()

    combi(0, 0)
    for arr in final:
        arr.sort(reverse=True)

    answer = calculate(final, numbers, operators)
    answer.sort(reverse=True)
    return answer[0]


if __name__ == "__main__":
    N = int(input())
    count_line = input().strip()
    numbers = []
    operators = []
    for i in range(N):
        if i % 2 == 0:
            numbers.append(int(count_line[i]))
        else:
            operators.append(count_line[i])
    print(solution(N, numbers, operators))
