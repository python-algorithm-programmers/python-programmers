N = 5
for start_y in range(N):
    for start_x in range(N):
        # 늘어날 수 있는 사이즈 계산
        dis = 0
        print()
        print("start_p", start_y, start_x)
        while True:
            dis += 1
            end_y = start_y+dis
            end_x = start_x+dis
            if end_y < N and end_x < N:
                print(dis, end_y, end_x)
            else:
                break