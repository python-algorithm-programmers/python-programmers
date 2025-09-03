def distance(a,b):
    y1, x1 = a
    y2, x2 = b
    return abs(y2-y1) + abs(x2-x1)

def dfs(idx, arc_cnt, arc_choice, total_choice):
    if arc_cnt == 3:
        total_choice.append(arc_choice[:])
        return

    if idx == M:
        return

    dfs(idx+1, arc_cnt, arc_choice, total_choice)
    arc_choice.append(idx)
    dfs(idx+1, arc_cnt+1, arc_choice, total_choice)
    arc_choice.pop()

def solution(N,M,D,maps):
    total_choice = []
    arc_choice = []
    dfs(0, 0, arc_choice, total_choice)
    best = []

    for archor_sel in total_choice:
        archor_kill_cnt = 0
        copy_maps = [mapss[:] for mapss in maps]

        # 턴 수 계산
        while True:
            archor_picks = set()
            for archor_x in archor_sel:
                archor_p = (N, archor_x)
                short_enemy_list = []
                # 적과의 거리 계산
                for y in range(N-1, -1, -1):
                    for x in range(M):
                        if copy_maps[y][x] == 1:
                            cur_dis = distance(archor_p, (y,x))
                            short_enemy_list.append((y,x,cur_dis))

                # 가장 가까운 적이면서 가장 왼쪽
                short_enemy_list.sort(key=lambda x:(x[2],x[1]))
                enemy_y, enemy_x, short_dis = short_enemy_list.pop(0)
                if D >= short_dis:
                    archor_picks.add((enemy_y, enemy_x))


            # 궁수들의 사격 확인 후 사살
            for pick in archor_picks:
                kill_y, kill_x = pick
                if copy_maps[kill_y][kill_x] == 1:
                    copy_maps[kill_y][kill_x] = 0
                    archor_kill_cnt += 1

            # 한칸씩 내려오기
            for y in range(N-1, -1, -1):
                for x in range(M):
                    if y == N-1:
                        copy_maps[y][x] = 0

                    else:
                        copy_maps[y+1][x] = copy_maps[y][x]

                    if y == 0:
                        copy_maps[y][x] = 0

            # map 안에 적이 없으면 종료
            if all(1 not in line for line in copy_maps):
                break

        best.append(archor_kill_cnt)

    best.sort()
    return best[-1]


if __name__ == "__main__":
    N,M,D = map(int, input().split())
    maps = []
    for _ in range(N):
       maps.append(list(map(int, input().split())))

    print(solution(N,M,D,maps))