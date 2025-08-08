import sys

if __name__ == "__main__":
    N = int(input())
    input_points = []
    meeting_points = []

    for _ in range(N):
        start, end = map(int, input().split())
        input_points.append([start, end])

    # 시간 순 정렬해줘야 회의실 시간 넣을 때 오른쪽 범위밖만 고려하면 됨
    input_points.sort(key=lambda x:(x[1],x[0]))

    for start, end in input_points:
        if not meeting_points:
            meeting_points.append([start, end])
            continue

        last_one = meeting_points[-1]

        # 겹치는 시간때가 없고 오른쪽 밖인 경우
        if last_one[1] <= start:
            meeting_points.append([start, end])

    #print(input_points)
    print(len(meeting_points))
