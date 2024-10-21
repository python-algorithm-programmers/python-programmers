def solution(N, numbers):
    # 중복 제거
    sorted_set = sorted(set(numbers))

    # dictionary_comprehension
    sorted_dict = {number: idx for idx, number in enumerate(sorted_set)}
    return [sorted_dict[number] for number in numbers]


if __name__ == '__main__':
    import sys
    lines = sys.stdin.readlines()
    N = lines[0].strip()
    number_list = lines[1].strip().split(" ")
    print(" ".join(map(str, solution(N, number_list))))