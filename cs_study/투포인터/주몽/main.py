def solution(N, M, input_list):
    input_list.sort()
    start, end = 0, len(input_list) - 1
    answer = 0
    while start < end:
        sum = input_list[start] + input_list[end]
        if sum == M:
            #print(input_list[start], input_list[end])
            answer += 1
            start += 1
        elif sum < M:
            start += 1
        else:
            end -= 1

    return answer

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    input_list = list(map(int, input().split()))
    print(solution(N, M, input_list))