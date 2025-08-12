def solution(N, M, K, maps, cur_dir, dir_choice):
    # 현재 위치, 냄새, 상어 목록
    cur_loc = [[] for _ in range(M+1)]                          # 1..M
    smell_maps = [[[0,0] for _ in range(N)] for _ in range(N)]  # [주인, 남은시간]
    cur_sharks = [i for i in range(1, M+1)]
    turn = 0

    # 초기 위치/냄새 세팅 (초기 냄새는 K)
    for i in range(1, M+1):
        for r in range(N):
            for c in range(N):
                if maps[r][c] == i:
                    cur_loc[i] = [r, c]
                    smell_maps[r][c] = [i, K]

    # 시뮬레이션
    while len(cur_sharks) > 1 and turn < 1000:
        turn += 1

        # 1) 이번 턴 이동 후보 모으기(이전 턴 냄새만 보고 결정)
        next_pos = {}            # (r,c) -> [여기로 오려는 상어 번호들]
        next_dir = [0]*(M+1)     # 각 상어의 새 방향
        new_loc  = [None]*(M+1)  # 각 상어의 새 좌표

        for i in cur_sharks[:]:  # 순회 중 삭제 영향 없게 사본으로
            r, c = cur_loc[i]
            pri_dirs = dir_choice[i][cur_dir[i]]  # 이 상어의 현재 방향 기준 우선순위 4개 (이미 (dy,dx))

            moved = False
            # 1-1) 빈 냄새 칸 우선
            for dy, dx in pri_dirs:
                ny, nx = r+dy, c+dx
                if 0 <= ny < N and 0 <= nx < N and smell_maps[ny][nx][0] == 0:
                    new_loc[i] = [ny, nx]
                    next_dir[i] = rev_dir[(dy,dx)]
                    next_pos.setdefault((ny, nx), []).append(i)
                    moved = True
                    break
            if moved:
                continue

            # 1-2) 없으면 자기 냄새 칸
            for dy, dx in pri_dirs:
                ny, nx = r+dy, c+dx
                if 0 <= ny < N and 0 <= nx < N and smell_maps[ny][nx][0] == i:
                    new_loc[i] = [ny, nx]
                    next_dir[i] = rev_dir[(dy,dx)]
                    next_pos.setdefault((ny, nx), []).append(i)
                    moved = True
                    break
            # 문제 조건상 항상 한 칸을 고를 수 있음

        # 2) 충돌 처리: 같은 칸이면 번호 작은 상어만 살림
        alive = []
        for cell, sharks in next_pos.items():
            winner = min(sharks)
            alive.append(winner)
        cur_sharks = sorted(alive)

        # 3) 냄새 감소
        for r in range(N):
            for c in range(N):
                if smell_maps[r][c][1] > 0:
                    smell_maps[r][c][1] -= 1
                    if smell_maps[r][c][1] == 0:
                        smell_maps[r][c][0] = 0

        # 4) 위치/방향 갱신 + 새 냄새 남김
        for i in cur_sharks:
            r, c = new_loc[i]
            cur_loc[i] = [r, c]
            cur_dir[i] = next_dir[i]
            smell_maps[r][c] = [i, K]

    return -1 if turn >= 1000 and len(cur_sharks) > 1 else turn

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