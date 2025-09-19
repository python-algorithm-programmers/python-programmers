from collections import deque

def batch(mon_where, mon_maps, num, mon_dicts, mon_size):
    start_x, start_y, end_x, end_y = mon_where

    for i in range(N):
        map_line = []
        for j in range(N):
            if start_y <= i < end_y and start_x <= j < end_x:
                mon_maps[i][j] = num
                map_line.append(mon_maps[i][j])

        if mon_dicts.get(num):
            if map_line:
                mon_dicts[num].appendleft(map_line)
        else:
            mon_dicts[num] = deque()
            if map_line:
                mon_dicts[num].appendleft(map_line)

    # 사이즈 계산
    size = 0
    for a in range(N):
        for b in range(N):
            if mon_maps[a][b] == num:
                size += 1
    mon_size[num] = size

    # 2개의 영역으로 나뉘는 지 확인
    if num > 1:
        item = list(mon_size.items())
        min_size, max_size = item[0][0], item[-1][0]
        for i in range(min_size, max_size+1):
            queue = deque()
            batch_visited = [[False]*N for _ in range(N)]
            queue_cnt = 0
            link_flag = False

            for r in range(N):
                if link_flag: break
                for c in range(N):
                    if link_flag: break
                    if mon_maps[r][c] == i and not batch_visited[r][c] and queue_cnt == 0:
                        queue.append((r,c))

                        while queue:
                            start_q_y, start_q_x = queue.popleft()
                            batch_visited[start_q_y][start_q_x] = True
                            for dy, dx in directions:
                                ny, nx = start_q_y+dy, start_q_x+dx
                                if 0 <= ny < N and 0 <= nx < N and not batch_visited[ny][nx] and mon_maps[ny][nx] == i:
                                    batch_visited[ny][nx] = True
                                    queue.append((ny, nx))

                        queue_cnt += 1

                    elif mon_maps[r][c] == i and not batch_visited[r][c] and queue_cnt >= 1:
                        link_flag = True

            # 두 부분으로 나뉘어 있으면 그 미생물 삭제
            if link_flag:
                # dict에서도 삭제
                mon_dicts.pop(i)
                mon_size.pop(i)

            # 맵에서 삭제할 지 추가할 지 설정
            size = 0
            new_mon_sticker = []
            for y in range(N):
                new_mon_line = []
                for x in range(N):
                    if mon_maps[y][x] == i:
                        if link_flag:
                            mon_maps[y][x] = 0
                        else:
                            size += 1
                            new_mon_line.append(mon_maps[y][x])

                if not link_flag:
                    if new_mon_line:
                        new_mon_sticker.append(new_mon_line)

            if not link_flag:
                mon_dicts[i] = deque(new_mon_sticker)
                mon_size[i] = size



def move(mon_maps, mon_size_item, mon_dicts, mon_size):
    for number, _ in mon_size_item:
        batch_flag = False
        for x in range(N):
            if batch_flag: break
            for y in range(N):
                # 배치가 됬다면 다음 것 탐색
                if batch_flag: break

                # 배치가 안되면 다음 곳으로 배치
                move_flag = False
                for r in range(len(mon_dicts[number])):
                    if move_flag: break
                    for c in range(len(mon_dicts[number][r])):
                        if y+r >= N or x+c >= N or mon_maps[y+r][x+c] != 0:
                            move_flag = True
                            break

                # 모두 배치가 가능한 것으로 확인되면, 그 때 배치
                # 그래서 배치하지 않는 것들은
                if not move_flag:
                    for r in range(len(mon_dicts[number])):
                        for c in range(len(mon_dicts[number][r])):
                            mon_maps[y + r][x + c] = mon_dicts[number][r][c]

                    batch_flag = True

        # 모두 배치를 못했으면 남은 것들 모두 삭제
        if not batch_flag:
            mon_dicts.pop(number)
            mon_size.pop(number)

def result(mon_maps, mon_size):
    answer = 0
    if len(mon_size.items()) == 1:
        return 0

    co_mon = set()
    for mon_num in mon_size.keys():
        visited = [[False] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if mon_maps[y][x] == mon_num and not visited[y][x]:
                    result_q = deque()
                    result_q.append((y,x))
                    while result_q:
                        res_y, res_x = result_q.popleft()
                        visited[res_y][res_x] = True

                        for dy, dx in directions:
                            ny, nx = dy+res_y, dx+res_x
                            if 0<=ny<N and 0<=nx<N and not visited[ny][nx] and mon_maps[ny][nx] == mon_num:
                                result_q.append((ny, nx))
                                visited[ny][nx] = True

                            # 옆에 다른 것을 찾았을 때
                            elif 0<=ny<N and 0<=nx<N and not visited[ny][nx] and mon_maps[ny][nx] != mon_num \
                                    and mon_maps[ny][nx] != 0:
                                co_mon.add((mon_num, mon_maps[ny][nx]))
                                visited[ny][nx] = True

    # tuple set에서 중복없이 근접한 세트끼리 곱셈을 합산
    for first_one, second_one in co_mon:
        answer += mon_size[first_one] * mon_size[second_one]

    return answer // 2


if __name__ == "__main__":
    N, Q = map(int, input().split())
    mon_maps = [[0]*N for _ in range(N)]
    num = 1
    mon_dicts = {1: deque()}
    mon_size = {1: 0}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for _ in range(Q):
        mon_where = list(map(int, input().split()))
        batch(mon_where, mon_maps, num, mon_dicts, mon_size)

        # 배치 이후 맵 초기화
        mon_maps = [[0]*N for _ in range(N)]

        # size 순으로 정렬
        mon_size_item = sorted(mon_size.items(), key=lambda x:x[1], reverse=True)
        move(mon_maps, mon_size_item, mon_dicts, mon_size)
        print(result(mon_maps, mon_size))
        num += 1
