"""
[조건]
수식 = + - *, 우선순위를 자유롭게 재정의 -> 가장 큰 숫자
같은 수식이면 앞에 있는 게 우선 순위
음수여도 절댓값으로 계산

1) 우선 순위 조합 만들기
2) 우선순위에 맞게, 앞에꺼부터 조건 적용하여 계산
"""


def dfs(idx, proceed, result, methods, visited):
    if idx == 3:
        if len(proceed) == 3:
            result.append(proceed[:])
        return

    for i in range(len(methods)):
        if not visited[i]:
            visited[i] = True
            proceed.append(methods[i])
            dfs(idx + 1, proceed, result, methods, visited)
            proceed.pop()
            visited[i] = False


def calculate(result, expression):
    def _cal_num(num1, num2, cal_method):
        #print(cal_method)
        if cal_method == "*":
            return num1 * num2
        elif cal_method == "+":
            return num1 + num2
        else:
            return num1 - num2

    # 1. 숫자와 계산을 리스트로 분리해두기
    num_list = []
    cal_list = []
    number = ""
    for char in expression:
        # 계산할 문자찾기
        if char not in [str(i) for i in range(10)]:
            num_list.append(int(number))
            number = ""
            cal_list.append(char)

        # 숫자값 기억해두기
        else:
            number += char

    # 마지막 숫자 담기
    num_list.append(int(number))

    # 2. 우선순위에 맞게 연산, 연산의 인덱스에 접근해서 그거 순서대로 접근해야됨
    # [100, 200, 300, 500, 20]
    # [-, *, -, +]
    best = 0
    for methods in result:
        # 매 연산마다 값을 바꿔서 계산해야하므로
        test = num_list[:]
        cal_test = cal_list[:]
        #print(methods)
        #print(cal_list)
        for method in methods:
            idx = 0
            #print(cal_test)
            while idx < len(cal_test):
                if cal_test[idx] == method:
                    calculated_num = _cal_num(test[idx], test[idx + 1], cal_test[idx])
                    # 계산 후, 값, 연산 삭제 후 삽입
                    test[idx] = calculated_num
                    test.pop(idx+1)
                    cal_test.pop(idx)
                else:
                    idx += 1

        if best < abs(test[0]):
            best = abs(test[0])

    return best


def solution(expression):
    proceed = []
    result = []
    methods = ["*", "-", "+"]
    visited = [False] * 3
    dfs(0, proceed, result, methods, visited)

    # 계산 적용
    best = calculate(result, expression)
    return best


if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print(solution(expression))