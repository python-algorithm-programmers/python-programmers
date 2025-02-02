def solution(input_list):
    cnt = 0
    d_cnt = 1

    # 더이상 증가할게 없을 때 멈춤
    while d_cnt != 0:
        d_cnt = 0
        for i in range(len(input_list)-1):
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                cnt += 1
                d_cnt = 1

    return input_list, cnt

if __name__ == "__main__":
    import sys
    sys.stdin = open('input.txt')
    input_list = list(map(int, input()[1:-1].split(', ')))
    print(solution(input_list))
