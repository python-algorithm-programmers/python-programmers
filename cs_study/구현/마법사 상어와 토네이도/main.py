def rotate(arr):
    return [list(arr) for arr in zip(*arr)][::-1]

def solution(maps):
    cur_loc = 0
    rotate_dir = [(0,-1), (-1,0), (0,1), (1,0)]
    y, x = center_y, center_x
    out_send_sum = 0
    sand_maps = [
        [0, 0, 2, 0, 0],
        [0, 10, 7, 1, 0],
        [5, 0, 0, 0, 0],
        [0, 10, 7, 1, 0],
        [0, 0, 2, 0, 0]
    ]

    for i in range(1, N+1):
        repeat = 2 if not i == N else 3
        for _ in range(repeat):
            if cur_loc == 4:
                cur_loc = 0
            dy, dx = rotate_dir[cur_loc]

            for _ in range(i):
                y, x = y+dy, x+dx
                if not (0<=y<N and 0<=x<N):
                    return out_send_sum

                # y 위치에 있는 모래는 사라질 예정
                sand = maps[y][x]
                if sand == 0:
                    continue

                maps[y][x] = 0
                out_sand = 0

                # 모래 바람을 평행 이동
                for r in range(5):
                    for c in range(5):
                        if sand_maps[r][c] == 0:
                            continue

                        p = sand_maps[r][c]
                        amount = sand * p // 100
                        out_sand += amount

                        # 2,2만큼 평행 이동
                        ny, nx = y + (r-2), x + (c-2)
                        if 0 <= ny < N and 0 <= nx < N:
                            maps[ny][nx] += amount
                        else:
                            out_send_sum += amount

                # 남은 알파 자리 계산
                alpha = sand - out_sand
                sand_y, sand_x = y+dy, x+dx
                if 0 <= sand_y < N and 0 <= sand_x < N:
                    maps[sand_y][sand_x] += alpha
                else:
                    out_send_sum += alpha

            sand_maps = rotate(sand_maps)
            cur_loc += 1

    return out_send_sum

if __name__ == "__main__":
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))

    center_y, center_x = N // 2, N // 2
    print(solution(maps))



