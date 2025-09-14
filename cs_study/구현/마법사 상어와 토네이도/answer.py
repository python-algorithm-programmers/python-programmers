def rotate(arr):
    # 90도 시계 회전: 다음 진행방향(왼→위→오→아래)에 맞춰 분배 패턴 회전
    return [list(row) for row in zip(*arr)][::-1]

def solution():
    cur_loc = 0
    rotate_dir = [(0,-1), (-1,0), (0,1), (1,0)]
    y, x = center_y, center_x
    out_send_sum = 0
    send_maps = [
        [0, 0, 2, 0, 0],
        [0, 10, 7, 1, 0],
        [5, 0, 0, 0, 0],
        [0, 10, 7, 1, 0],
        [0, 0, 2, 0, 0]
    ]

    for i in range(1, N+1):
        repeat = 3 if i == N else 2
        for _ in range(repeat):
            if cur_loc == 4:
                cur_loc = 0
            dy, dx = rotate_dir[cur_loc]

            for _ in range(i):
                y, x = y+dy, x+dx
                if not (0 <= y < N and 0 <= x < N):
                    return out_send_sum

                sand = maps[y][x]
                if sand == 0:
                    continue
                maps[y][x] = 0

                moved = 0
                for r in range(5):
                    for c in range(5):
                        p = send_maps[r][c]
                        if p == 0:
                            continue
                        ny, nx = y+(r-2), x+(c-2)
                        amount = (sand * p) // 100
                        moved += amount
                        if 0 <= ny < N and 0 <= nx < N:
                            maps[ny][nx] += amount
                        else:
                            out_send_sum += amount

                ny, nx = y+dy, x+dx
                alpha = sand - moved
                if 0 <= ny < N and 0 <= nx < N:
                    maps[ny][nx] += alpha
                else:
                    out_send_sum += alpha

            send_maps = rotate(send_maps)  # 반시계 회전
            print(maps)
            cur_loc += 1

    return out_send_sum

if __name__ == "__main__":
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    center_y, center_x = N // 2, N // 2
    print(solution())