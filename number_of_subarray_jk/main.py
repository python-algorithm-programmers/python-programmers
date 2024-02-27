def combination(list, n):
    result = []
    for i in range(0, len(list) - n):
        sum_sub = sum(list[i:i+n+1])
        result.append(sum_sub)
    return result



def solution(elements):
    answer_list = []

    # 길이가 1 ~ n까지 나눠서 합을 set로 추가하기
    for i in range(len(elements)):
        subarray = elements

        # 연속합을 구할 리스트 추가하기
        subarray = subarray + [elements[j] for j in range(i)]

        # 연속된 조합으로 합을 구하기
        answer_list.extend(combination(subarray, i))

    answer_set = set(answer_list)
    return len(answer_set)

if __name__ == '__main__':
    print(solution([7,9,1,1,4]))
