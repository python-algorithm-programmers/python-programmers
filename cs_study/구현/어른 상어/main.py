def solution(N, M, K, maps, cur_dir, dir_choice):
    cur_loc = [[] for _ in range(M+1)]
    smell_maps = [[[0,0] for _ in range(N)] for _ in range(N)]
    cur_sharks = [i for i in range(1, M+1)]
    turn = 0
    end_flag = False

    # 상어들 현재 위치 확인
    for i in range(1, M+1):
        for r in range(N):
            for c in range(N):
                if maps[r][c] == i:
                    cur_loc[i] = [r,c]
                    smell_maps[r][c] = [i, K-1]

    while len(cur_sharks) > 1 and turn < 1000:
        turn += 1

        #

        # 가능한 탐색하고, 있으면 이동하고 먹고
        # 없으면 자기꺼로 돌아오도록
        for i in range(1, len(cur_sharks)):
            for r in range(N):
                if end_flag: break
                for c in range(N):
                    if end_flag: break
                    directions = dir_choice[i][cur_dir[i]]

                    for dy, dx in directions:
                        ny, nx = r+dy, c+dx

                        if 0<=ny<N and 0<=nx<N:
                            # 빈 공간으로 존재할 때
                            if smell_maps[ny][nx][0] == 0:
                                smell_maps[ny][nx]=[i,K]
                                # 현재 몸방향 설정
                                for k, v in dir_mapper.items():
                                    find_dy, find_dx = v
                                    if find_dy==dy and find_dx==dx:
                                        cur_dir[i] = k
                                end_flag = True
                                break

                            # 먼저 선수 쳤을 때
                            # 순서가 작은 거부터이므로 이미 늦은 상황
                            elif smell_maps[ny][nx][1] == K and smell_maps[ny][nx][0] != i:
                                # 값으로 삭제
                                cur_sharks.remove(i-1)

                                # 인덱스로 삭제
                                #cur_sharks.pop(i)
                                end_flag = True
                                break

                            # 갈 수 있는 곳이 없을 때
                            elif smell_maps[ny][nx][0] == i:
                                smell_maps[ny][nx] = [i, K]
                                # 현재 몸방향 설정
                                for k, v in dir_mapper.items():
                                    find_dy, find_dx = v
                                    if find_dy == dy and find_dx == dx:
                                        cur_dir[i] = k
                                end_flag = True
                                break

        # 시간 지날 때마다 냄새 한칸씩 줄이기
        for r in range(N):
            for c in range(N):
                if smell_maps[r][c][0] != 0:
                    if smell_maps[r][c][1] > 0:
                        smell_maps[r][c][1] -= 1
                        # 냄새 카운트가 끝나면 초기화
                        if smell_maps[r][c][1] == 0:
                            smell_maps[r][c][0] = 0

    if turn == 1000:
        return -1

    return turn


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))

    # 현재 몸 방향 지정, 인덱스가 1일 때 1번부터 지정하는 것을 목표
    cur_dir = list(map(int, input().split()))
    cur_dir.insert(0,0)
    dir_mapper = {
        1: (-1,0),
        2: (1, 0),
        3: (0, -1),
        4: (0, 1)
    }
    rev_dir = {v: k for k, v in dir_mapper.items()}

    # 몸방향 별 우선순위 저장 딕셔너리
    dir_choice = {}
    for i in range(1,M+1):
        for j in range(1,5):
            if not dir_choice.get(i):
                dir_choice[i] = {}
            if not dir_choice[i].get(j):
                dir_choice[i][j] = []

            # 여기서 상하좌우를 좌표료 변경
            raw_dirs = list(map(int, input().split()))
            real_dirs = []
            for raw_dir in raw_dirs:
                real_dirs.append(dir_mapper[raw_dir])
            dir_choice[i][j] = real_dirs

    print(solution(N, M, K, maps, cur_dir, dir_choice))

