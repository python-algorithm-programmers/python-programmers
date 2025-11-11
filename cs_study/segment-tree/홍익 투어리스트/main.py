
# move_loc과 제일 가까운 idx 찾기
def find_bisect(maps_idx, move_loc, N):
    if not maps_idx:
        return -1

    left, right = 0, len(maps_idx) - 1
    answer = None
    #print("maps_idx", maps_idx)
    #print("move_loc", move_loc)
    while left <= right:
        mid = (left + right) // 2
        #print("lrm", left, right, mid)
        # 이후
        if maps_idx[mid] >= move_loc:
            answer = maps_idx[mid]
            right = mid - 1

        # 이전
        else:
            #answer = maps_idx[mid]
            left = mid + 1

    if answer is not None:
        return answer - move_loc

    # 다음 사이클에 있는 경우
    return (maps_idx[0] - move_loc) % N


if __name__ == "__main__":
    import sys
    import bisect
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    maps = list(map(int, input().split()))
    maps_idx = sorted([i for i in range(len(maps)) if maps[i] == 1])
    move_loc = 0

    for _ in range(Q):
        cmd_list = list(map(int, input().split()))
        command = cmd_list[0]
        # 명소 지정 해제
        if command == 1:
            sights = cmd_list[1]
            if maps[sights-1] == 1:
                maps[sights - 1] = 0
                maps_idx.remove(sights - 1)
            else:
                maps[sights - 1] = 1
                bisect.insort(maps_idx, sights - 1)

        # 시계방향 이동
        elif command == 2:
            move_loc = (move_loc + cmd_list[1]) % N

        # 최소 몇 칸 움직이는 지확인
        else:
            print(find_bisect(maps_idx, move_loc, N))
            #print()

