def rotate(arr):
    # 반시계 90도 (원래 그대로 사용)
    return [list(row) for row in zip(*arr)][::-1]

def solution(maps):
    cur_loc = 0
    rotate_dir = [(0,-1), (-1,0), (0,1), (1,0)]  # 왼, 위, 오, 아래 (반시계 진행)
    y, x = center_y, center_x
    out_send_sum = 0

    # '왼쪽 진행' 기준 5x5 분배 (α 제외, 합계 45% — 5% 포함!)
    sand_maps = [
        [0, 0, 2, 0, 0],
        [0,10, 7, 1, 0],
        [5, 0, 0, 0, 0],
        [0,10, 7, 1, 0],
        [0, 0, 2, 0, 0]
    ]

    for i in range(1, N+1):
        repeat = 3 if i == N else 2
        for _ in range(repeat):
            if cur_loc == 4:
                cur_loc = 0
            dy, dx = rotate_dir[cur_loc]

            for _ in range(i):
                y, x = y + dy, x + dx
                if not (0 <= y < N and 0 <= x < N):
                    return out_send_sum

                sand = maps[y][x]
                if sand == 0:
                    maps[y][x] = 0
                    continue

                maps[y][x] = 0
                moved = 0

                # 5x5 분배 (r, c 로! 바깥 i 섀도잉 금지)
                for r in range(5):
                    for c in range(5):
                        p = sand_maps[r][c]
                        if p == 0:
                            continue
                        ny, nx = y + (r - 2), x + (c - 2)
                        amount = (sand * p) // 100
                        moved += amount
                        if 0 <= ny < N and 0 <= nx < N:
                            maps[ny][nx] += amount
                        else:
                            out_send_sum += amount

                # α(나머지) → 진행 방향 한 칸
                ny, nx = y + dy, x + dx
                alpha = sand - moved
                if 0 <= ny < N and 0 <= nx < N:
                    maps[ny][nx] += alpha
                else:
                    out_send_sum += alpha

            # 다음 방향으로 갈 때, 패턴은 '시계 90°' 회전 필요
            # (rotate는 반시계이므로 3번 적용해서 시계 효과)
            sand_maps = rotate(rotate(rotate(sand_maps)))
            cur_loc += 1

    return out_send_sum

if __name__ == "__main__":
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    center_y, center_x = N // 2, N // 2
    print(solution(maps))