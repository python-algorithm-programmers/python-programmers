from collections import Counter


def solution(str1, str2):
    # 1. 모두 소문자화
    str1 = str1.lower()
    str2 = str2.lower()

    group1, group2 = [], []

    # 2. 2글자씩 자르기
    for i in range(len(str1)-1):
        # 특수 문자가 포함되어있는 지 확인
        if 97 > ord(str1[i]) or ord(str1[i]) > 122:
            continue
        if 97 > ord(str1[i+1]) or ord(str1[i+1]) > 122:
            continue
        s = str1[i:i+2]
        group1.append(s)

    for j in range(len(str2)-1):
        if 97 > ord(str2[j]) or ord(str2[j]) > 122:
            continue
        if 97 > ord(str2[j+1]) or ord(str2[j+1]) > 122:
            continue
        t = str2[j:j+2]
        group2.append(t)

    # 3. 교집합 구하기
    counter1 = Counter(group1)
    counter2 = Counter(group2)
    common_list = list((counter1 & counter2).elements())
    common_size = len(common_list)
    print(common_list)

    # 4. 합집합 구하기
    add_list = list((counter1 | counter2).elements())
    add_size = len(add_list)
    print(add_list)


    # 5. 값 구하기
    if add_size == 0 or common_size == 0:
        return 65536

    return 65536 * common_size // add_size


if __name__ == "__main__":
    # print(ord('z'))
    print(solution("FRANCE", "french"))
    # print(solution('handshake', 'shake hands'))