import re
from collections import Counter

def get_similarity(list1, list2):
    # 합집합 구하기
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    union = list((counter1 | counter2).elements())

    # 교집합 구하기
    intersection = list((counter1 & counter2).elements())

    # # 교집합 구하기
    # intersection = []
    # for word in list1:
    #     if word in list2:
    #         intersection.append(word)
    #         list2.remove(word)

    # print(f'counter1 ={counter1}')
    # print(f'counter2 ={counter2}')
    # print(f'union ={union}')
    # print(f'intersection ={intersection}')
    return 65536 * len(intersection) // len(union) if len(union) != 0 else 65536

def make_array(words):
    total_list = []
    # 2글자씩 읽기
    for i in range(len(words)-1):
        word = words[i:i+2]

        # 숫자, 공백이나 특수 문자가 있다면 다음꺼로 진행
        if re.search(r'[\d_\s\W]', word):
            continue
        else:
            total_list.append(word)
    return total_list

def solution(str1, str2):

    # 대소문자 차이는 무시 -> 모두 대문자로 바꿔서 읽기
    str1, str2 = str1.upper(), str2.upper()

    list1, list2 = make_array(str1), make_array(str2)
    return get_similarity(list1, list2)

if __name__ == '__main__':
    print(solution("aa1+aa2", "AAAA12"))