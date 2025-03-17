def solution(input_list):
    # head , number, tail 구분
    # 리스트 내부에 또다른 리스트를 두고 그 리스트에 tuple 값을 넣어서 작성
    file_name_list = []
    number_list = [str(num) for num in range(10)]
    for file_name in input_list:
        head, number, tail = '', '', ''
        head_flag, number_flag, tail_flag = True, False, False

        for char in file_name:
            # head
            if char not in number_list and head_flag:
                if not number_flag:
                    number_flag = True
                head += char
                continue

            # number
            if char in number_list and number_flag:
                if head_flag:
                    head_flag = False
                if not tail_flag:
                    tail_flag = True
                number += char
                continue

            # tail
            if char not in number_list and tail_flag:
                if number_flag:
                    number_flag = False
                tail += char

        # 소문자화 해서 head 저장
        head = head.lower()

        # 숫자화 해서 number 저장
        number = int(number)
        file_name_list.append((file_name, (head, number, tail)))

    # 정렬
    # head 순서대로, 그다음 number 순서대로
    file_name_list.sort(key=lambda x: (x[1][0], x[1][1]))

    return [k for k,v in file_name_list]

if __name__ == "__main__":
    input_list = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    print(solution(input_list))