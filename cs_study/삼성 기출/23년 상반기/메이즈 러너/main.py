from pprint import pprint

def calculate(start_p, end_p):
    start_y, start_x = start_p
    end_y, end_x = end_p
    return abs(end_y-start_y) + abs(end_x-start_x)

def solution(N, M, K, user_map, maze, exit):
    total_distance = [0]
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    end_flag = [False]

    # 이동
    def move():
        #print(exit)
        exit_y, exit_x = exit
        user_keys = list(user_map.keys())
        for user_idx in user_keys:
            user_y, user_x = user_map[user_idx]
            cur_dis = calculate((user_y, user_x), exit)
            candidate_moves = []
            dy_flag = False
            for dy, dx in directions:
                if dy != 0:
                    dy_flag = True
                ny, nx = user_y+dy, user_x+dx
                next_dis = calculate((ny, nx), exit)
                #print("user", user_idx)
                #print(cur_dis, next_dis)
                if 0 <= ny < N and 0 <= nx < N \
                    and maze[ny][nx] == 0 \
                    and next_dis < cur_dis:
                    candidate_moves.append((next_dis, dy_flag, ny, nx))

            # 움직임 여부 판단
            if candidate_moves:
                total_distance[0] += 1
                candidate_moves.sort(key=lambda x:(x[0], -x[1]))
                #print("candidate_moves", candidate_moves)
                _, _, next_y, next_x = candidate_moves[0]
                user_map[user_idx] = [next_y, next_x]

                if exit_y == next_y and exit_x == next_x:
                    del user_map[user_idx]

                    if not user_map:
                        end_flag[0] = True

    # 벽 회전 이동
    """
    [출구와 참가자 최소 1명을 포함한 가장 작은 정사각형 구하기]
    - r이 작은 것 -> c가 작은 것
    
    [90도 회전]
    - 벽과 사용자, 출구 모두
    - 90도 회전
    
    [내구도 감소 시키기]
    """
    def rotate_map():
        """가장 작은 정사각형 뽑기"""
        # 출구와 유저 한명이상 포함해서 가장 작은 정사각형
        exit_y, exit_x = exit
        user_loc = []
        user_keys = list(user_map.keys())
        for user_key in user_keys:
            user_y, user_x = user_map[user_key]
            user_loc.append((user_y, user_x, user_key))

        # 유저 좌표 리스트, y -> x 순으로 정렬
        user_loc.sort(key=lambda x:(x[0], x[1]))

        # 좌표 하나씩 뽑아보면서, 정사각형 되는 지 확인
        candidate_square = []
        for user_y, user_x, _ in user_loc:
            #print("user")
            #print(user_y, user_x)

            # 정사각형 만들기
            # 시작점 찾기
            for start_y in range(N):
                for start_x in range(N):
                    dis = 0
                    while True:
                        dis += 1
                        end_y = start_y + dis
                        end_x = start_x + dis
                        user_contained = False
                        exit_contained = False
                        # 범위안 이면서
                        if end_y < N and end_x < N:
                            # 안에 포함되는 지 확인
                            for y in range(start_y, end_y+1):
                                for x in range(start_x, end_x+1):
                                    if user_y == y and user_x == x:
                                        user_contained = True

                                    if exit_y == y and exit_x == x:
                                        exit_contained = True

                                    if user_contained and exit_contained:
                                        candidate_square.append((dis + 1, start_y, start_x, end_y, end_x))
                        else:
                            break

        # 크기 -> y, x 순으로 정렬
        candidate_square.sort(key=lambda x:(x[0], x[1], x[2]))
        #print("candidate_square", candidate_square)
        """ 
        정사각형 리스트 새로 만들고
        출구, 벽, 포함되는 사람 넣고 90도 회전
        내구도 감소
        """
        dis, start_y, start_x, end_y, end_x = candidate_square[0]
        new_arr = [[[] for _ in range(dis)] for _ in range(dis)]
        for r in range(start_y, end_y+1):
            for c in range(start_x, end_x+1):
                if maze[r][c] > 0:
                    new_arr[r-start_y][c-start_x].append(maze[r][c] - 1)
                    # 맵에서 지움
                    maze[r][c] = 0

                # 사람도 추가
                for user_y, user_x, user_idx in user_loc:
                    if r == user_y and c == user_x:
                        new_arr[r - start_y][c - start_x].append(user_idx)

                # 출구도 추가, 100으로 추가
                if r == exit_y and c == exit_x:
                    new_arr[r - start_y][c - start_x].append(100)

        # 시계 방향 90도 회전
        new_arr = list(map(list, zip(*new_arr[::-1])))

        # 회전 시킨 맵 적용
        # 이때, 사람과 출구 빼고 넣어야함
        for r in range(start_y, end_y + 1):
            for c in range(start_x, end_x + 1):
                if new_arr[r-start_y][c-start_x]:
                    # 출구 찾은 경우 반영하고 지움
                    if new_arr[r-start_y][c-start_x][0] == 100:
                        exit[0], exit[1] = r, c
                        continue

                    # 벽 찾은 경우만 원래 맵에 반영
                    # 이미 벽에 해당한 부분들은 0으로 치웟으므로 정사각형 구간은 0
                    if 0 < new_arr[r - start_y][c - start_x][0] <= 9:
                        maze[r][c] = new_arr[r - start_y][c - start_x][0]
                        continue

                    # 사람 찾은 경우, 반영하고 지움
                    for find_user in new_arr[r-start_y][c-start_x]:
                        if 10 <= find_user < 100:
                            user_map[find_user] = [r, c]

    for k in range(K):
        #print("turn", k+1)
        move()
        if end_flag[0]:
            #print("result")
            print(total_distance[0])
            print(exit[0]+1, exit[1]+1)
            break

        #print("before rotate")
        #pprint(maze)
        #print("exit", exit)
        #print("user_map", user_map)
        rotate_map()

        #print("after rotate")
        #pprint(maze)
        #print("exit", exit)
        #print("user_map", user_map)
        #print()

    if not end_flag[0]:
       #print("result")
        print(total_distance[0])
        print(exit[0] + 1, exit[1] + 1)


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    user_map = {}
    maze = []
    for _ in range(N):
        map_line = list(map(int, input().split()))
        maze.append(map_line)

    for i in range(10, M+10):
        r, c = map(int, input().split())
        user_map[i] = [r-1, c-1]

    exit_y, exit_x = map(int, input().split())
    exit = [exit_y-1, exit_x-1]
    solution(N, M, K, user_map, maze, exit)

