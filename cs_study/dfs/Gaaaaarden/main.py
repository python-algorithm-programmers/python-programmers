from collections import deque
def bfs(reds, greens, N, M, maps):
    # dfs에서 배열을 초기화할 수 없으므로 bfs 시작 때 초기화
    area = [[[0, 0] for _ in range(M)] for _ in range(N)]
    seconds = 0
    flower_cnt = 0
    r_queue = deque()
    g_queue = deque()
    directions = [
        (1,0), (0,1), (-1,0), (0,-1)
    ]

    # 빨강, 초록 배양액 위치 정보 큐에 넣기
    for red_y, red_x in reds:
        r_queue.append((red_y, red_x))
        area[red_y][red_x] = [3, 0]

    for green_y, green_x in greens:
        g_queue.append((green_y, green_x))
        area[green_y][green_x] = [4, 0]

    # 초 단위로 확장되는 것을 확인
    # 동시에 확장되어야 꽃이 핌
    while r_queue and g_queue:
        seconds +=1
        # area에 [색깔, 초]로 기록해서 같은 초에 있다면 꽃으로 바꾸고 탐색종료
        # 이렇게 하면 green, red 따로 돌려도 됨
        # red 부터
        for _ in range(len(r_queue)):
            red_y, red_x = r_queue.popleft()
            for dy, dx in directions:
                r_ny, r_nx = red_y + dy, red_x + dx
                if 0 <= r_ny< N and 0 <= r_nx < M and maps[r_ny][r_nx] != 0 and area[r_ny][r_nx][0] == 0:
                    area[r_ny][r_nx] = [3, seconds]
                    r_queue.append((r_ny,r_nx))

        for _ in range(len(g_queue)):
            green_y, green_x = g_queue.popleft()
            for dy, dx in directions:
                g_ny, g_nx = green_y + dy, green_x + dx
                if 0 <= g_ny< N and 0 <= g_nx < M and maps[g_ny][g_nx] != 0:
                    if area[g_ny][g_nx][0] == 0:
                        area[g_ny][g_nx] = [4, seconds]
                        g_queue.append((g_ny, g_nx))

                    # 이미 red에서 동시간대에 선점을 친 경우
                    # 꽃은 확장할 수 없으니 큐에 추가하지 않음
                    if area[g_ny][g_nx][0] == 3 and area[g_ny][g_nx][1] == seconds and maps[g_ny][g_nx]==1:
                        area[g_ny][g_nx] = [5, seconds]
                        flower_cnt += 1

    return flower_cnt


# 선택만을 위한 dfs를 결정해야함
# 더불어서 배양액을 온전히 다 뿌린다음에 bfs를 적용하는 게 맞음
def dfs(idx, g_cnt, r_cnt, best, reds, greens, N, M, G, R, maps, index_soil):
    if g_cnt == G and r_cnt == R:
        flower_cnt = bfs(reds, greens, N, M, maps)
        best[0] = max(flower_cnt, best[0])
        return

    # 인덱스가 다되도 return
    if idx == len(index_soil):
        return

    # 칸 건너뛰어도 되니 칸 건너뛰기
    dfs(idx+1, g_cnt, r_cnt, best, reds, greens, N, M, G, R, maps, index_soil)

    # 토양에 뿌리기
    y,x = index_soil[idx]

    # 초록 뿌리기
    if g_cnt < G:
        greens.append((y,x))
        dfs(idx+1, g_cnt+1, r_cnt, best, reds, greens, N, M, G, R, maps, index_soil)
        greens.pop()

    if r_cnt < R:
        reds.append((y,x))
        dfs(idx+1, g_cnt, r_cnt+1, best, reds, greens, N, M, G, R, maps, index_soil)
        reds.pop()


def solution(N, M, G, R, maps):
    best = [0]
    # 호수 0, 토양 1, 배양 2
    # 초록 배양액 3, 빨강 배양액 4, 꽃은 5

    index_soil = []
    for i in range(N):
        for j in range(M):
            if maps[i][j]==2:
                index_soil.append((i,j))
    dfs(0, 0, 0, best, [], [], N, M, G, R, maps, index_soil)
    return best[0]

if __name__ == "__main__":
    N, M, G, R = list(map(int, input().split(" ")))
    maps = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, M, G, R, maps))
