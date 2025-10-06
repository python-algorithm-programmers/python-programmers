def solution(new_id):
    # 1. 소문자화
    new_id.lower()

    # 2. -, _, . 빼기
    next_id = ""
    test_num = [str(i) for i in range(0, 10)]
    for char in new_id:
        if ord('a') <= ord(char) <= ord('z') or char in ['-', '_', '.'] or char in test_num:
            next_id += char

    # 3. 마침표가 연속으로 나오면 중복 제거
    third_id = ""
    flag = False
    for check in next_id:
        if check == ".":
            # 딱 한번만 마침표 넣기
            if not flag:
                flag = True
                third_id += check

        else:
            flag = False
            third_id += check

    next_id = third_id
    # 4. 맨앞, 맨뒤에 있으면 빼기
    if next_id:
        if next_id[0] == ".":
            next_id = next_id[1:]

        if next_id[-1] == ".":
            next_id = next_id[:-1]

    # 5. 빈문자열이면, a 대입
    if not next_id:
        next_id = "a"

    # 6. 16자 보다 길면 15자까지 자르기
    if len(next_id) >= 16:
        next_id = next_id[:16]

    # 7. 2자 이하라면 마지막 문자를 길이가 3 될때까지 끝에 붙임
    if len(next_id) <= 2:
        last_char = next_id[-1]
        while len(next_id) < 3:
            next_id += last_char

    return next_id


if __name__ == "__main__":
    new_id = 	"abcdefghijklmn.p"
    print(solution(new_id))