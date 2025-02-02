# 인덱스로 두고
# 맨 마지막 인덱스는 정렬이 되었다고 생각하고 넘김

input_list = [4, 6, 2, 9, 1]

def solution(input_list):
    n = len(input_list)

    # 총 비교하는 인덱스가 n, n-1, n-2 .... 2까지 가므로
    for i in range(n-1):
        # 내부에서 확인하는 것도 n - 1 - i까지 임
        for j in range(n-1-i):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]

    return input_list

print(solution(input_list))

