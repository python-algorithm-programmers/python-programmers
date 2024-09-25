def solution(s):
    cnt = 1
    zero_cnt = 0
    non_zero_char = ''
    while True:
        # 0을 제거
        for char in s:
            if char != '0':
                non_zero_char += char
            else:
                zero_cnt += 1

        # 종료 조건
        if non_zero_char == '1':
            break

        # 2 -> 길이의 수(10) 변환
        len_char = len(non_zero_char)
        print(len_char)

        # 10진 수 -> 2진법
        binary_char = bin(len_char)[2:]
        print(binary_char)
        cnt += 1

        # s로 초기화 시켜서 for 문에서 재실행되도록
        s = binary_char

        # 받을 바구니도 초기화
        non_zero_char = ''

    return [cnt, zero_cnt]

if __name__ == '__main__':
    print(solution("110010101001"))