import heapq
import sys
def solution(N, input_points):
    cls_room = []
    for start, end in input_points:
        if not cls_room:
            heapq.heappush(cls_room, (end, start))
            continue

        first_one = cls_room[0]
        if start >= first_one[0]:
            heapq.heappop(cls_room)

        heapq.heappush(cls_room, (end, start))
    return len(cls_room)


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    input_points = []
    for _ in range(N):
        input_points.append(list(map(int, sys.stdin.readline().strip().split())))

    # 정렬
    input_points.sort(key=lambda x:(x[0], x[1]))
    print(solution(N, input_points))