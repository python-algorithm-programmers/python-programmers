def solution(N, numbers):
    result_dict = {i:[] for i in range(N)}
    for i in range(N):
        max_check_list = []
        for j in range(i):
            if numbers[j] < numbers[i]:
                # 이전 인덱스의 배열을 그대로 가져와서 현재 숫자를 붙임
                # 파이썬 내 리스트는 이렇게 작업이 가능함
                new_seq = result_dict[j] + [numbers[i]]
                max_check_list.append(new_seq)

        # 전보다 작은 게 없는 경우엔 그냥 본인 자신 추가
        if not max_check_list:
            result_dict[i] = [numbers[i]]

        else:
            result_dict[i] = max(max_check_list, key=len)

    # 제일 긴 것을 떼기
    longest_seq = max(result_dict.values(), key=len)
    print(len(longest_seq))
    print(" ".join(map(str, longest_seq)))


if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline().strip())
    numbers = list(map(int, sys.stdin.readline().strip().split(" ")))
    solution(N, numbers)