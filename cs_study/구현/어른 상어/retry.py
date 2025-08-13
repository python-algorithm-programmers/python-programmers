def solution(N, M, K, maps, cur_dir, dir_order):
    smell_maps = [[[0,0] for _ in range(N)] for _ in range(N)]
    cur_place = [[0,0] for _ in range(M+1)]
    # 초기 냄새 설정 및 현재 위치 확인
    for r in range(N):
        for c in range(N):
            if maps[r][c] != 0:
                shark_num = maps[r][c]
                smell_maps[r][c] = [shark_num, K-1]
                cur_place[shark_num] = [r,c]

    turn = 0
    sharks_list = [i for i in range(1,M+1)]
    while len(sharks_list) > 1:
        # 이동
        # 현재 위치를 보고 차례대로 상어대로 확인
        for shark_idx in sharks_list[:]:
            end_flag = False
            start_y, start_x = cur_place[shark_idx]
            directions = dir_order[shark_idx][cur_dir[shark_idx]]
            for direction in directions:
                dy, dx = dir_mapper[direction]
                ny, nx = start_y+dy, start_x+dx

                if 0<=ny<N and 0<=nx<N:
                    # 빈공간이 있는 경우
                    if smell_maps[ny][nx][0] == 0:
                        smell_maps[ny][nx].append(shark_idx)

                        # 현재 위치, 현재 방향으로 세팅
                        cur_place[shark_idx] = [ny,nx]
                        cur_dir[shark_idx] = direction
                        end_flag = True
                        break

            if end_flag: continue
            for direction in directions:
                dy, dx = dir_mapper[direction]
                ny, nx = start_y + dy, start_x + dx

                if 0 <= ny < N and 0 <= nx < N:
                    # 빈공간이 없는 경우, 무조건 자기 쪽에만 가야함
                    if smell_maps[ny][nx][0] == shark_idx:
                        smell_maps[ny][nx] = [shark_idx, K]

                        # 현재 위치, 현재 방향으로 세팅
                        cur_place[shark_idx] = [ny, nx]
                        cur_dir[shark_idx] = direction
                        break

        for r in range(N):
            for c in range(N):
                # 만약 상어끼리 같은 자리에 와서 누적이 된 경우
                if len(smell_maps[r][c]) > 2:
                    remove_sharks = smell_maps[r][c][3:]
                    for remove_shark in remove_sharks:
                        sharks_list.remove(remove_shark)

                    # race_condition 발생한 자리 냄새 배분
                    smell_maps[r][c] = [smell_maps[r][c][2],K]

                # 냄새 줄이기
                if smell_maps[r][c][0] != 0:
                    smell_maps[r][c][1] -= 1

                # 초기화
                if smell_maps[r][c][1] == 0:
                    smell_maps[r][c][0] = 0

        turn += 1
        if turn == 1000:
            return -1

    return turn

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))

    # 현재 몸 방향
    cur_dir = [0]
    cur_dir.extend(list(map(int, input().split())))

    # 상어별 몸방향 우선순위
    dir_order = {i:{} for i in range(1, M+1)}
    for i in range(1, M+1):
        for j in range(1,5):
            dir_order[i].setdefault(j, []).extend(list(map(int, input().split())))

    dir_mapper = {
        1: (-1, 0),
        2: (1, 0),
        3: (0, -1),
        4: (0, 1)
    }

    print(solution(N, M, K, maps, cur_dir, dir_order))
