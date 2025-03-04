# 땅을 밟을 지 말지까지 고민하지 않아도 되므로
# 4 * 3^(N-1)만큼 가짓수가 생김
# 4개의 행 중 하나를 선택한다는  -> dp로 풀어야함
def solution(land):
    n = len(land)
    # 값 참조여서 dp_list나 land나 동일하게 작용
    # dp_list = land

    # 최적의 값만 저장하도록 해야함
    for i in range(1, n):
        for j in range(4):
            tmp = land[i-1][j]
            land[i-1][j] = -1
            land[i][j] += max(land[i-1][0], land[i-1][1], land[i-1][2], land[i-1][3])
            land[i - 1][j] = tmp

    return max(land[n-1])


if __name__ == "__main__":
    land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
    print(solution(land))