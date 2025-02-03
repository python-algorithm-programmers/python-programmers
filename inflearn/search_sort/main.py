def solution(input_list):
    n = len(input_list)

    for i in range(n-1):
        min_index = i
        for j in range(1, n-i):
            if input_list[i+j] < input_list[min_index]:
                min_index = i+j
                input_list[i], input_list[min_index] = input_list[min_index], input_list[i]

    return input_list

if __name__ == "__main__":
    import sys
    sys.stdin = open("input.txt")
    input_list = list(map(int, input()[1:-1].split(", ")))
    print(solution(input_list))


#