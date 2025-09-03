from collections import deque


def solution(N, maps):
    visited = [[False]*N for _ in range(N)]
    # 0이 가로 1은 대각선 2는 세로의 body position
    pos_dir = {0: [(0,1), (1,1)], 1: [(0,1), (1,1), (1,0)], 2: [(1,1), (1,0)]}
    dest_cnt = 0
    queue = deque()
    queue.append((0,1,0))
    while queue:
        for _ in range(len(queue)):
            cur_loc_y, cur_loc_x, cur_pos = queue.popleft()
            for dy, dx in pos_dir[cur_pos]:
                ny, nx = cur_loc_y+dy, cur_loc_x+dx
                # print(cur_loc_y, cur_loc_x)
                # print(cur_pos)
                # print(dy, dx)
                # print()

                # 만약 ny,nx가 N-1까지 도달했으면 queue에 넣지않고 바로 카운트
                if ny == N-1 and nx == N-1:
                    # print("----answer---")
                    dest_cnt += 1
                    # print(cur_loc_y, cur_loc_x)
                    # print(cur_pos)
                    # print(dy, dx)
                    # print(pos_dir[cur_pos])
                    # print()
                    continue

                if dy==1 and dx==1:
                    if 0<=ny<N and 0<=nx<N and maps[ny][nx]==0 \
                            and maps[cur_loc_y][cur_loc_x+1] == 0 and maps[cur_loc_y+1][cur_loc_x]==0:
                        queue.append((ny,nx, 1))
                    continue

                elif dy==0 and dx==1: next_pos = 0
                else: next_pos = 2

                if 0 <= ny < N and 0 <= nx < N and \
                    maps[ny][nx]==0:
                    queue.append((ny, nx, next_pos))

    return dest_cnt

if __name__ == "__main__":
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().strip().split())))

    print(solution(N, maps))