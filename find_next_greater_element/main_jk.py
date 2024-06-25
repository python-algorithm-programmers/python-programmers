
def solution(numbers):
    answer = [-1] * len(numbers)
    # 리스트로 구현 가능
    # 원소들을 없애서 계산 속도를 줄이되, 인덱스 위치 정보는 필요하므로
    # 인덱스 정보만 stack에 담기
    stack = []

    # 뒷방향: 뒤에 오는 원소들을 모두 비교하여 O(n^2)의 복잡도 -> queue
    # 앞방향: 원소를 하나 떼어내어 이전의 원소하고만 비교하는 O(n)의 복잡도 -> stack

    for i, number in enumerate(numbers):
        while stack and number > numbers[stack[-1]]:
            last = stack.pop()
            answer[last] = number

        stack.append(i)
    return answer


if __name__ == '__main__':
    print(solution([9, 1, 5, 3, 6, 2]))