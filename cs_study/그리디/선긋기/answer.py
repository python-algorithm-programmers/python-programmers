import sys
if __name__ == "__main__":
    line_points = []
    input_points = []
    N = int(sys.stdin.readline().strip())
    answer = 0

    for _ in range(N):
        line = sys.stdin.readline().strip()
        start, end = map(int, line.split())
        input_points.append([start, end])

    # 정렬해줘야 앞에서 받으면서, 맨 마지막꺼만 조회해서 비교가능
    input_points.sort(key=lambda x:(x[0],x[1]))

    for start, end in input_points:
        if not line_points:
            line_points.append([start, end])
            continue

        # 마지막꺼만 빼서 비교
        last_one = line_points[-1]

        # 순서대로 정렬했으니 시작 부분은 당연히, 작은 거부터이니 왼쪽 포함관계는 없음
        # 크기 순서대로 차례로 뽑았으니 오른쪽 확장만 고려
        # 포함된 경우
        if last_one[0] <= start <= end <= last_one[1]:
            continue

        # 오른쪽 확장
        elif last_one[0] <= start <= last_one[1] <= end:
            line_points[-1][1] = end

        else:
            line_points.append([start, end])

    for line_point in line_points:
        answer += line_point[1] - line_point[0]
    print(answer)