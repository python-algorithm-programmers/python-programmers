def solution(n, left, right):
    # 이차원 배열 컴프리헨션
    # two_arrays = [[max(i+1, j+1) for j in range(n)] for i in range(n)]

    # 1차원 배열화
    two_arrays = [max(i + 1, j + 1) for j in range(n) for i in range(n)]

    # 특정 인덱스의 것만 불러오기
    answer = [two_arrays[i] for i in range(left,right+1)]
    return answer

if __name__ == '__main__':
    print(solution(3,2,5))