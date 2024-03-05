def solution(phone_book):
    # key값만 사용함
    phone_dict = {phone: True for phone in phone_book}

    for phone in phone_book:

        # 글자수 딱 맞춰서 동일한 게 있는 지를 확인하기 위해
        # 이중 for 문구성
        temp = ''
        for phone_num in phone:
            temp += phone_num

            # dict에 있는 완전한 번호면서, 자기 자신 말고 다른 것을 택하도록 해야함
            if temp in phone_dict and temp != phone:
                return False

    return True

if __name__ == '__main__':
    print(solution(["123", "456", "789"]))