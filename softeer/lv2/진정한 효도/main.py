def solution(maps):
    # 최댓값 설정
    min_effort = 50

    # 세로(X)부터 실시
    for i in range(len(maps)):
        first, second, third = maps[0][i], maps[1][i], maps[2][i]
        # 서로 같은 2개가 없는 경우
        if (first != second) and (second != third) and (third != first):
            effort = 2
            if min_effort > effort:
                min_effort = effort

        # 그에 반대는 다른 공통된 2개가 있다는 것
        else:
            # 다른 한개만 동일하게 만들어주면 됨
            if first != second:
                effort = abs(first-second)

            elif first != third:
                effort = abs(first - third)

            else:
                effort = abs(second - third)

            if min_effort > effort:
                min_effort = effort

    # 가로
    for j in range(3):
        first, second, third = maps[j][0], maps[j][1], maps[j][2]
        # 서로 같은 2개가 없는 경우
        if (first != second) and (second != third) and (third != first):
            effort = 2
            if min_effort > effort:
                min_effort = effort

        # 그에 반대는 다른 공통된 2개가 있거나 모두 동일하다는 것
        else:
            # 다른 한개만 동일하게 만들어주면 됨
            if first != second:
                effort = abs(first - second)

            elif first != third:
                effort = abs(first - third)

            # 다른 한개 다른 것이거나 모두 같은 경우 처리
            else:
                effort = abs(second - third)

            if min_effort > effort:
                min_effort = effort

    return min_effort

if __name__ == "__main__":
    import sys
    lines = sys.stdin.readlines()
    maps = [list(map(int, line.strip().split(" "))) for line in lines]
    print(solution(maps))