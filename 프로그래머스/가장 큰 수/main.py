def solution(numbers):
    # 숫자 늘려서 저장하기
    numbers_list = []
    longest = max(map(str,numbers), key=len)
    longest_len = len(longest)

    # 동일한 숫자 늘려 붙이기
    for number in numbers:
        number_str = str(number)
        last_str_number = number_str[-1]
        number_len = len(number_str)

        if number_len < longest_len:
            for __ in range(longest_len - number_len):
                number_str += last_str_number

        numbers_list.append((str(number), number_str))

    # 정렬
    sorted_numbers_list = sorted(numbers_list, key=lambda x: x[1], reverse=True)
    if sorted_numbers_list[0][0] == '0':
        return '0'

    # 숫자 표현
    return ''.join([k for k, v in sorted_numbers_list])


if __name__ == "__main__":
    numbers = [12, 1213]
    print(solution(numbers))