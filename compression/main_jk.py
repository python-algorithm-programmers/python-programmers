from collections import deque

def solution(msg):
    # 각 문자별 사전번호 추가
    alphabet_dict = {}
    for i in range(0, 26):
        alphabet_dict[chr(ord('A') + i)] = i+1

    # 문자를 한글자~있는 글자수만큼 읽어가면서 없으면 value값 반환 + 사전 등록
    msg_list = list(msg)
    answer = []

    i = 0
    while msg_list:
        alphabet = ''.join(msg_list[:i + 1])
        if alphabet in alphabet_dict :
            # 종료 조건
            if len(msg_list) == i + 1:
                answer.append(alphabet_dict[alphabet])
                return answer

            # 다음 인덱스까지 추가해서 글자 추가
            i += 1
            continue

        else:
            max_value = max(alphabet_dict.values())
            # 새 알파벳 등록
            alphabet_dict[alphabet] = max_value + 1

            # 이전 알파벳의 숫자값 넣기
            before_alphabet = ''.join(msg_list[:i])
            answer.append(alphabet_dict[before_alphabet])
            msg_list = msg_list[i:]

            # 인덱스 초기화
            i = 0

if __name__ == '__main__':
    print(solution("TOBEORNOTTOBEORTOBEORNOT"))