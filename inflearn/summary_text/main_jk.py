def solution(strs):
    alpha_dict = {}
    for char in strs:
        alpha_dict[char] = alpha_dict.get(char, 0) + 1

    last_str = ''
    for k, v in alpha_dict.items():
        last_str += k
        last_str += str(v)
        last_str += '/'

    return last_str[:-1]


if __name__ == "__main__":
    import sys
    sys.stdin = open('input.txt')
    str_text = input().strip()
    print(solution(str_text))