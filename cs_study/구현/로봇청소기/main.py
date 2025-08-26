def solution(N,M,cur_loc,cur_dir,directions,d_to_dir,maps):
    clean_cnt = 0
    while True:
        # 현재 위치 청소
        back_flag = True
        cur_y, cur_x = cur_loc
        if maps[cur_y][cur_x] == 0:
            maps[cur_y][cur_x] = 2
            clean_cnt += 1

        # 현재 방향으로 90도 회전하며 4방향 탐색
        cur_dir_t = cur_dir
        for _ in range(4):
            next_dir = cur_dir_t - 1
            if next_dir == -1:
                next_dir = 3
            dy, dx = d_to_dir[next_dir]
            ny, nx = cur_y+dy, cur_x+dx

            if 0<=ny<N and 0<=nx<N and maps[ny][nx] == 0:
                cur_loc = [ny, nx]
                cur_dir = next_dir
                back_flag = False
                # 방향과 현재위치 정하고 탐색 종료
                break

            # 다음 방향 갱신 (왼쪽으로 회전)
            cur_dir_t = next_dir

        # 4방향 다 돌았는 데 없는 경우
        if back_flag:
            back_dir = (cur_dir+2) % 4

            # 후진 가능 여부 확인
            back_dy, back_dx = d_to_dir[back_dir]
            ny, nx = back_dy+cur_y, back_dx+cur_x
            # 벽만 아니면 후진되니깐 2도 허용
            if 0 <= ny < N and 0 <= nx < N and maps[ny][nx] != 1:
                cur_loc = [ny, nx]
            else:
                return clean_cnt

if __name__ == "__main__":
    N, M = map(int, input().split())
    cur = list(map(int, input().split()))
    cur_loc, cur_dir = [cur[0], cur[1]], cur[2]
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    d_to_dir = {i:directions[i] for i in range(4)}
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))

    print(solution(N,M,cur_loc,cur_dir,directions,d_to_dir,maps))