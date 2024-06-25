from collections import Counter

def solution(k, tangerine):
    # 딕셔너리로 풀기
    count = Counter(tangerine)
    tangerine_list = []

    # dictionary를 튜플로 바꿔서 value 기준으로 내림차순 정렬
    sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

    # [key]*value 만큼 존재하는 배열 생성하고 리스트에 추가
    for key,value in sorted_items:
        arr = [key] * value
        tangerine_list.extend(arr)

    count = 1
    for i in range(k):
        if i > 0 and tangerine_list[i] != tangerine_list[i - 1]:
            count += 1

    return count

if __name__ == '__main__':
    print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))