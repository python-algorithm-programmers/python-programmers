def solution(input_dict):
    sorted_list = sorted(input_dict.items(), key=lambda x:(x[1][0], x[1][1]))
    for key, v_tuple in sorted_list:
        if int(v_tuple[0]) <= 4 and int(v_tuple[0]) > 0:
            print(key)

if __name__ == "__main__":
    import sys
    lines = sys.stdin.readlines()
    input_dict = {}
    for line in lines:
        s = line.strip()
        if '.' in s:
            input_dict[s] = tuple(map(int,(line.strip().split("."))))
        else:
            input_dict[s] = (int(s),-1)
    solution(input_dict)
