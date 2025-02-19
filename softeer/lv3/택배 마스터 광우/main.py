from functools import reduce
def solution(scores, routine_list):
    result = 0
    for start, end in routine_list:
        sum = reduce(lambda x,y: x+y, scores[start-1:end])
        list_len = len(scores[start-1:end])
        # 반올림 직전 1의 자리 수 보기
        big_num = sum * 1000 // list_len
        if big_num % 10 >= 5:
            big_num = big_num + (10 - big_num % 10)
        else:
            big_num = big_num - (big_num % 10)
        print(big_num / 1000)
    return result

if __name__ == "__main__":
    import sys
    input_data = list(map(int, sys.stdin.readline().strip().split(" ")))
    N = input_data[0]
    K = input_data[1]

    scores = list(map(int, sys.stdin.readline().strip().split(" ")))
    routine_list = []
    for __ in range(K):
        routine = list(map(int, sys.stdin.readline().strip().split(" ")))
        routine_list.append((routine[0], routine[1]))

    solution(scores, routine_list)