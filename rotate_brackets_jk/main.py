def solution(s):
    str = s
    result = 0
    # 글자 돌리기

    for i in range(len(s)):
        idx = 0
        while idx < len(str):
            if idx == 0 and (str[idx] == ']' or str[idx] == '}' or str[idx] == ')'):
                break

            if str[idx] == ']':
                if '[' == str[idx-1]:
                    str = str[:idx-1] + str[idx+1:]
                    idx -= 1
                    continue

            elif str[idx] == '}':
                if '{' == str[idx-1]:
                    str = str[:idx-1] + str[idx+1:]
                    idx -= 1
                    continue

            elif str[idx] == ')':
                if '(' == str[idx-1]:
                    str = str[:idx-1] + str[idx+1:]
                    idx -= 1
                    continue

            idx += 1

        if not str:
            result += 1

        str = s[i+1:len(s)] + s[:i+1]

    return result

if __name__ == '__main__':
    print(solution("[)(]"))