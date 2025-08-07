import sys
if __name__ == "__main__":
    line_points = []
    N = int(sys.stdin.readline().strip())
    append_flag = False
    answer = 0

    for _ in range(N):
        line = sys.stdin.readline().strip()
        start, end = map(int, line.split())

        if not line_points:
            new_line = [start, end]
            line_points.append(new_line)
            continue

        # 구간이 여러 군데로 나뉠 수 있으므로 for문 적용
        for line_point in line_points:
            append_flag = False

            # 1. 한 개의 구간이라도 포함되었는 지, 왼쪽 확장
            if start <= line_point[0] <= end <= line_point[1]:
                line_point[0] = start
                append_flag = True
                break
            # 오른쪽 확장
            elif line_point[0] <= start <= line_point[1] <= end:
                line_point[1] = end
                append_flag = True
                break

            # 2. 아예 포함해버렷는 지 확인
            elif start <= line_point[0] and end >= line_point[1]:
                line_point[0] = start
                line_point[1] = end
                append_flag = True
                break

            # 2-1, 포함된 경우라면
            elif start >= line_point[0] and end <= line_point[1]:
                append_flag = True
                break

        # 3. 연결된 구간이 아예 없음
        if not append_flag:
            next_line = [start, end]
            line_points.append(next_line)

    for line_point in line_points:
        answer += line_point[1] - line_point[0]
    print(answer)