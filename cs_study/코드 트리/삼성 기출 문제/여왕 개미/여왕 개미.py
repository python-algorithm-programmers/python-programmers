import sys
input = sys.stdin.readline

Q = int(input())
houses = []   # 현재 존재하는 개미집 좌표 (정렬 유지)

for _ in range(Q):
    cmd = list(map(int, input().split()))
    t = cmd[0]

    if t == 100:  # 마을 건설
        N = cmd[1]
        houses = [0] + cmd[2:]   # 여왕 집(0) 포함
    elif t == 200:  # 개미집 건설
        p = cmd[1]
        houses.append(p)
    elif t == 300:  # 개미집 철거
        q = cmd[1] - 1  # 1-index → 0-index
        houses.pop(q)
    elif t == 400:  # 개미집 정찰
        r = cmd[1] - 1  # 1-index → 0-index
        if not houses:   # 개미집이 없다면
            print(0)
            continue

        # 정찰할 개미집 좌표
        pos = houses[r]

        # 현재 존재하는 가장 왼쪽, 오른쪽 개미집
        left = houses[0]
        right = houses[-1]

        # 왕복 시간: 해당 좌표까지 갔다가 돌아오기
        # → 양 끝 중 더 가까운 쪽까지 갔다 오는 시간
        ans = min(abs(pos - left), abs(right - pos)) * 2
        print(ans)