def solution(N, input_points):
    # 강의실 배열
    cls_rooms = [[] for _ in range(N)]

    for start, end in input_points:
        for i in range(N):
            if not cls_rooms[i]:
                cls_rooms[i].append([start, end])
                break

            last_one = cls_rooms[i][-1]
            if last_one[1] <= start:
                cls_rooms[i].append([start, end])
                break

            # 그 시간과 겹치는 경우 (포함, 일부 포함하고 초과)
            else:
                continue

    answer = 0
    for room in cls_rooms:
        if room:
            answer += 1
    return answer

if __name__ == "__main__":
    N = int(input())
    input_points = []
    for _ in range(N):
        input_points.append(list(map(int, input().split())))

    # 정렬
    input_points.sort(key=lambda x:(x[0],x[1]))
    print(solution(N, input_points))