"""
0. solution() 메서드를 큰 줄기로 쓰기
1. 분할 메서드
2. 올바른 문자열인지 확인 메서드
"""


def is_correct(p):
    stack = []
    for char in p:
        if char == "(":
            stack.append(char)

        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False

    return True


def uv_split(p):
    one_cnt, second_cnt = 0, 0
    for i, char in enumerate(p):
        if char == "(":
            one_cnt += 1
        else:
            second_cnt += 1

        if one_cnt == second_cnt:
            return p[:i + 1], p[i + 1:]


def solution(p):
    if not p:
        return p

    u, v = uv_split(p)
    if is_correct(u):
        return u + solution(v)

    else:
        temp = "(" + solution(v) + ")"
        temp_list = []
        for char in u[1:-1]:
            if char == "(":
                temp_list.append(")")
            else:
                temp_list.append("(")

        return temp + "".join(temp_list)


