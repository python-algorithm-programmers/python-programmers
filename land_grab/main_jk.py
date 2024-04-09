def solution(land):
    for i in range(1,len(land)):
        for j in range(4):
            # 같은 인덱스인 경우는 선택할 수 없으므로
            # MAX 값 결정 시, 아예 -1을 만들어서 고려하지 않도록 설계
            tmp = land[i-1][j]
            land[i-1][j] = -1

            # 다음 줄에 차근히 더해가는 방식으로
            land[i][j] += max(land[i-1][0], land[i-1][1], land[i-1][2], land[i-1][3])

            # 다른 인덱스의 경우도 최댓값을 정해야하니 이전 줄의 -1값을 초기화
            land[i - 1][j] = tmp

    return max(land[i][0], land[i][1], land[i][2], land[i][3])

if __name__ == '__main__':
    print(solution([[6, 7, 1, 2], [2, 3, 10, 8], [1, 3, 9, 4], [7, 11, 4, 9]]))