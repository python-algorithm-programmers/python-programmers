from collections import deque
from pprint import pprint
import heapq
def solution(N, K, L, dust_maps, robot_loc):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 큐에 담을 때, 시간 단축 필요함
    def move():
        # 다른 로봇이 있는 위치는 탐색하지 못한므로 리스트로 받아서 queue에 넣을 때 배제
        # 자기 자신은 구분할 수 있도록 idx 꼭 포함해서, retain 그러면 빼도 됨

        # 제자리에서도 굳이 다른 곳 가지 않고 탐색할 수 있음, 이것을 반영
        # 자기 자신은 빼기
        for robot_idx, robot_info in robot_loc.items():
            robot_y, robot_x, robot_dir = robot_info
            robot_where = [(r_info[0], r_info[1]) for r_idx, r_info in robot_loc.items() if r_info != robot_info]

            target = []
            visited = [[False]*N for _ in range(N)]
            queue = deque([(0, robot_y, robot_x)])

            # 현재 위치에서도 탐색하기, 이전에 바뀐 로봇의 위치가 아닌 경우
            if dust_maps[robot_y][robot_x] > 0 and (robot_y, robot_x) not in robot_where:
                robot_loc[robot_idx] = [robot_y, robot_x, robot_dir]
                continue

            while queue:
                dis, start_y, start_x = queue.popleft()
                if target and dis > target[0][0]:
                    break

                visited[start_y][start_x] = True
                for dy, dx in directions:
                    ny, nx = start_y+dy, start_x+dx
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and dust_maps[ny][nx] != -1 and (ny, nx) not in robot_where:
                        # 먼지 발견
                        if dust_maps[ny][nx] > 0:
                            # 같은 깊이인 애들은 참조
                            heapq.heappush(target, (dis+1, ny, nx))

                        queue.append((dis+1, ny, nx))
                        visited[ny][nx] = True

            #print(target)

            # 해당 ny, nx로 이동
            if not target:
                continue
            else:
                target.sort(key=lambda x: (x[0], x[1], x[2]))
                final_dis, target_y, target_x = target[0]
                robot_loc[robot_idx] = [target_y, target_x, robot_dir]
            # 청소기가 도달한 곳은 -2로 지정
            # retain.append([target_y, target_x, dust_maps[target_y][target_x]])
            # dust_maps[target_y][target_x] = -2
            #print()

        # for target_y, target_x, fundament in retain:
        #     dust_maps[target_y][target_x] = fundament

    def clean():
        for robox_idx, robot_info in robot_loc.items():
            robot_y, robot_x, robot_dir = robot_info

            target_dir = []
            for i in range(4):
                total = 0
                before = (i-1) % 4
                cur = i
                after = (i+1) % 4

                # 자기 자리
                my_add = dust_maps[robot_y][robot_x]
                if my_add > 20:
                    my_add = 20
                total += my_add

                # 다른 방향
                for find_dir in [before, cur, after]:
                    dy, dx = directions[find_dir]
                    ny, nx = robot_y+dy, robot_x+dx

                    if 0 <= ny < N and 0 <= nx < N and dust_maps[ny][nx] > 0:
                        add = dust_maps[ny][nx]
                        if add > 20:
                            add = 20
                        total += add

                target_dir.append((total, i))
            target_dir.sort(key=lambda x:(-x[0], x[1]))

            # 해당 방향에서 청소기로 청소 진행
            #print(target_dir)
            _, final_dir = target_dir[0]
            cur = final_dir
            before = (cur - 1) % 4
            after = (cur + 1) % 4

            # 자기 자신도 먼지 삭제
            if dust_maps[robot_y][robot_x] > 0:
                dust_maps[robot_y][robot_x] -= 20
                if dust_maps[robot_y][robot_x] < 0:
                    dust_maps[robot_y][robot_x] = 0

            # 다른 방향
            for k in [before, cur, after]:
                dy, dx = directions[k]
                ny, nx = robot_y+dy, robot_x+dx
                if 0 <= ny < N and 0 <= nx < N:
                    if dust_maps[ny][nx] > 0:
                        dust_maps[ny][nx] -= 20
                        if dust_maps[ny][nx] < 0:
                            dust_maps[ny][nx] = 0

    def dust_add():
        for i in range(N):
            for j in range(N):
                if dust_maps[i][j] > 0:
                    dust_maps[i][j] += 5

    def populate(dust_maps):
        # 청소기 위치에는 먼지 확산이 안됨
        # for robot_idx, robot_info in robot_loc.items():
        #     robot_y, robot_x, robot_dir = robot_info

        new_maps = [row[:] for row in dust_maps]
        for y in range(N):
            for x in range(N):
                populate_dust = 0
                if dust_maps[y][x] == 0:
                    for dy, dx in directions:
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < N and 0 <= nx < N and dust_maps[ny][nx] > 0:
                            populate_dust += dust_maps[ny][nx]

                    # 10으로 나눈 값
                    new_maps[y][x] = populate_dust // 10

        return new_maps

    def record():
        sum_dust = 0
        for i in range(N):
            for j in range(N):
                if dust_maps[i][j] > 0:
                    sum_dust += dust_maps[i][j]
        return sum_dust


    for _ in range(L):
        #print("move_before", robot_loc)
        move()
        #print("move_after", robot_loc)

        #print("before clean")
        #pprint(dust_maps)

        clean()
        #print("after clean")
        #pprint(dust_maps)

        dust_add()
        #print("before populate")
        #pprint(dust_maps)

        new_map = populate(dust_maps)
        dust_maps = new_map
        #print(dust_maps)
        pprint(record())
        #print("after populate")
        #pprint(dust_maps)
        #print()


if __name__ == "__main__":
    N, K, L = map(int, input().split())
    dust_maps = []
    for _ in range(N):
        dust_maps.append(list(map(int, input().split())))

    robot_loc = {}
    for i in range(K):
        r, c = map(int, input().split())
        robot_loc[i] = [r-1, c-1, 0]

    solution(N, K, L, dust_maps, robot_loc)