def solution(s):
    stack = []
    for char in s:
        if not stack:
            stack.append(char)

        elif stack[-1] == char:
            stack.pop()

        else:
            stack.append(char)

    if len(stack):
        return 0

    else:
        return 1

if __name__ == '__main__':
    print(solution("baabaa"))