def solution(s):
    # 문자열 파싱: 집합 기호 제거해서 숫자들만 str값으로 분리하여 리스트 저장
    elements = s[2:-2].split('},{')

    # 크기순으로 정렬한 뒤에 for문으로 하나씩 불러서 원소
    sorted_list = sorted(elements, key=lambda x:len(x))

    answer = []
    last_str = False

    for num_str in sorted_list:
        if not last_str:
            answer.append(int(num_str))
            last_str = True

        else:
            for str in num_str.split(','):
                if int(str) not in answer:
                    answer.append(int(str))

    return answer

if __name__ == '__main__':
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))