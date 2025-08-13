def solution(N, M, K, maps, cur_dir, dir_order):
    smell_maps = [[[0,0] for _ in range(N)] for _ in range(N)]
    cur_place = [[0,0] for _ in range(M+1)]

    # 초기 냄새: K 로 시작 (기존 K-1 → K)
    for r in range(N):
        for c in range(N):
            if maps[r][c] != 0:
                shark_num = maps[r][c]
                smell_maps[r][c] = [shark_num, K]   # ← 여기 수정
                cur_place[shark_num] = [r,c]

    turn = 0
    sharks_list = [i for i in range(1,M+1)]
    while len(sharks_list) > 1:

        # -----------------------
        # 1) 모든 상어 이동: 후보만 쌓기
        # -----------------------
        for shark_idx in sharks_list[:]:
            start_y, start_x = cur_place[shark_idx]
            directions = dir_order[shark_idx][cur_dir[shark_idx]]

            moved = False
            # (a) 빈칸 우선
            for direction in directions:
                dy, dx = dir_mapper[direction]
                ny, nx = start_y+dy, start_x+dx
                if 0<=ny<N and 0<=nx<N and smell_maps[ny][nx][0] == 0:
                    smell_maps[ny][nx].append(shark_idx)   # 후보만 쌓기
                    cur_place[shark_idx] = [ny, nx]
                    cur_dir[shark_idx] = direction
                    moved = True
                    break

            # (b) 빈칸 없으면 자기 냄새로 (여기도 append만!)
            if not moved:
                for direction in directions:
                    dy, dx = dir_mapper[direction]
                    ny, nx = start_y+dy, start_x+dx
                    if 0<=ny<N and 0<=nx<N and smell_maps[ny][nx][0] == shark_idx:
                        smell_maps[ny][nx].append(shark_idx)   # ← 기존의 [id,K] 대입을 append로 변경
                        cur_place[shark_idx] = [ny, nx]
                        cur_dir[shark_idx] = direction
                        break

        # -----------------------
        # 2) 먼저 기존 냄새 1 감소
        # -----------------------
        for r in range(N):
            for c in range(N):
                if smell_maps[r][c][0] != 0 and smell_maps[r][c][1] > 0:
                    smell_maps[r][c][1] -= 1
                    if smell_maps[r][c][1] == 0:
                        smell_maps[r][c][0] = 0  # 냄새 소멸

        # -----------------------
        # 3) 충돌/단독 도착 처리 + 새 냄새 K 로 세팅
        # -----------------------
        for r in range(N):
            for c in range(N):
                if len(smell_maps[r][c]) > 2:
                    candidates = smell_maps[r][c][2:]
                    winner = min(candidates)  # 가장 작은 번호 승리
                    # 패자 제거
                    for s in candidates:
                        if s != winner and s in sharks_list:
                            sharks_list.remove(s)
                    # 칸을 승자 냄새로 확정
                    smell_maps[r][c] = [winner, K]
                else:
                    # 후보가 없으면 (len==2) 그대로 유지 (owner, ttl)
                    # 단, len>2가 아닌 칸에서 오래된 append 찌꺼기가 남지 않도록 보장됨
                    pass

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
