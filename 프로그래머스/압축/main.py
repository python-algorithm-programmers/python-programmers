from collections import deque


def solution(msg):
    index_dict = {chr(ord('A')+i): i+1 for i in range(26)}
    alphabet_queue = deque(msg)
    result = []
    last_number = 26

    while alphabet_queue:
        # 다음 글자까지도 있는 지 확인
        present_q = alphabet_queue.popleft()
        find_str = present_q

        while alphabet_queue:
            find_str += alphabet_queue[0]
            if not index_dict.get(find_str):
                last_number += 1
                index_dict[find_str] = last_number
                find_str = find_str[:-1]
                break
            alphabet_queue.popleft()

        # 결과 추가하기
        result.append(index_dict.get(find_str))

    return result


if __name__ == "__main__":
    msg = "ABABABABABABABAB"
    print(solution(msg))

