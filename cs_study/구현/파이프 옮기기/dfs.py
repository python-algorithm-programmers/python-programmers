import sys


def dfs(y, x, pos_dir, cur_pos, dest_cnt):
    if y == N-1 and x == N-1:
        dest_cnt[0] += 1
        return

    for dy, dx in pos_dir[cur_pos]:
        ny, nx = y+dy, x+dx

        if ny > N - 1 or nx > N - 1:
            continue

        if dy == 1 and dx == 1:
            if maps[y][x + 1] == 0 and maps[y + 1][x] == 0 and maps[ny][nx] == 0:
                dfs(ny, nx, pos_dir, 1, dest_cnt)

        elif dy == 0 and dx == 1:
            if maps[ny][nx] == 0:
                dfs(ny, nx, pos_dir, 0, dest_cnt)

        else:
            if maps[ny][nx] == 0:
                dfs(ny, nx, pos_dir, 2, dest_cnt)

def solution(N, maps):
    pos_dir = {0: [(0, 1), (1, 1)], 1: [(0, 1), (1, 1), (1, 0)], 2: [(1, 1), (1, 0)]}
    dest_cnt = [0]
    dfs(0, 1, pos_dir, 0, dest_cnt)
    return dest_cnt[0]

if __name__ == "__main__":
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, sys.stdin.readline().strip().split())))

    print(solution(N, maps))