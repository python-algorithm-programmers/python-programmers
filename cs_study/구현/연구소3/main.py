def rotate(vectors):
    return [(dx, -dy) for dy, dx in vectors]
def dfs(points_idx, points, choices, total_choices):
    if points_idx == len(points):
        total_choices.append(choices[:])
        return

    for i in range(4):
        y, x, cctv = points[points_idx]
        choices.append((y, x, cctv, i))
        dfs(points_idx+1, points, choices, total_choices)
        choices.pop()

def solution(N,M,maps):
    cctv_cam = {
        1: [(0,1)],
        2: [(0,-1), (0,1)],
        3: [(-1,0), (0,1)],
        4: [(0,-1), (-1,0), (0,1)],
        5: [(0,-1), (-1,0), (0,1), (1,0)]
    }
    points = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] in [a for a in range(1,6)]:
                points.append((i,j,maps[i][j]))
    choices, total_choices = [], []
    dfs(0, points, choices, total_choices)

    best_cnt = []
    for choice_sel in total_choices:
        # 조합마다 초기화할 대상
        visited = [[False] * M for _ in range(N)]
        copy_maps = [row[:] for row in maps]

        for y, x, cctv, rotate_num in choice_sel:
            rotated_vectors = cctv_cam[cctv]
            for _ in range(rotate_num):
                rotated_vectors = rotate(rotated_vectors)

            for dy, dx in rotated_vectors:
                for multi in range(8):
                    ny, nx = y+dy*multi, x+dx*multi
                    if ny>=N or nx >=M:
                        break
                    # 벽에 막힐 때
                    if 0<=ny<N and 0<=nx<M and copy_maps[ny][nx] == 6:
                        break
                    elif 0<=ny<N and 0<=nx<M and copy_maps[ny][nx] == 0:
                        copy_maps[ny][nx] = 7
                        visited[ny][nx] = True

        # 갯수 세기
        cnt = 0
        for i in range(N):
            for j in range(M):
                if copy_maps[i][j] == 0:
                    cnt += 1
        best_cnt.append(cnt)

    #print(best_cnt)
    best_cnt.sort()
    return best_cnt[0]


if __name__ == "__main__":
    N, M = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    print(solution(N,M,maps))