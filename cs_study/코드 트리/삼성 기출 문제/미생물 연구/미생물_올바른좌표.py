from collections import deque

def batch(mon_where, mon_maps, num, mon_dicts, mon_size):
    start_x, start_y, end_x, end_y = mon_where
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for i in range(N-1, -1, -1):
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
    for a in range(N-1, -1, -1):
        for b in range(N):
            if mon_maps[a][b] == num:
                size += 1
    mon_size[num] = size

    # 2개의 영역으로 나뉘는 지 확인
    if num > 1:
        for i in range(1, num+1):
            queue = deque()
            visited = [[False]*N for _ in range(N)]
            queue_cnt = 0
            link_flag = False

            for r in range(N-1, -1, -1):
                if link_flag: break
                for c in range(N):
                    if link_flag: break
                    if mon_maps[r][c] == i and not visited[r][c] and queue_cnt == 0:
                        queue.append((r,c))

                        while queue:
                            start_q_y, start_q_x = queue.popleft()
                            visited[start_q_y][start_q_x] = True
                            for dy, dx in directions:
                                ny, nx = start_q_y+dy, start_q_x+dx
                                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                                    visited[ny][nx] = True
                                    queue.append((ny, nx))

                        queue_cnt += 1

                    elif mon_maps[r][c] == i and not visited[r][c] and queue_cnt >= 1:
                        link_flag = True

            # 두 부분으로 나뉘어 있으면 그 미생물 삭제
            if link_flag:
                # dict에서도 삭제
                mon_dicts.pop(num)
                mon_size.pop(num)

            # 맵에서 삭제할 지 추가할 지 설정
            size = 0
            for y in range(N-1, -1, -1):
                mon_line = []
                for x in range(N):
                    if mon_maps[y][x] == i:
                        if link_flag:
                            mon_maps[y][x] = 0
                        else:
                            size += 1
                            mon_line.append(mon_maps[y][x])

                if not link_flag:
                    mon_dicts[num].append(mon_line)

            if not link_flag:
                mon_size[num] = size



def move(mon_maps, mon_size_item, mon_dicts, mon_size):
    for number, _ in mon_size_item:
        batch_flag = False
        for x in range(N):
            if batch_flag: break
            for y in range(N-1, -1, -1):
                # 배치가 됬다면 다음 것 탐색
                if batch_flag: break

                # 배치가 안되면 다음 곳으로 배치
                move_flag = False
                for r in range(len(mon_dicts[number])):
                    if move_flag: break
                    for c in range(len(mon_dicts[number][r])):
                        if y-r < 0 or x+c >= N or mon_maps[y-r][x+c] != 0:
                            move_flag = True
                            break

                # 모두 배치가 가능한 것으로 확인되면, 그 때 배치
                # 그래서 배치하지 않는 것들은
                if not move_flag:
                    for r in range(len(mon_dicts[number])):
                        for c in range(len(mon_dicts[number][r])):
                            mon_maps[y - r][x + c] = mon_dicts[number][r][c]

                    batch_flag = True

        # 모두 배치를 못했으면 남은 것들 모두 삭제
        if not batch_flag:
            mon_dicts.pop(number)
            mon_size.pop(number)



if __name__ == "__main__":
    N, Q = map(int, input().split())
    mon_maps = [[0]*N for _ in range(N)]
    num = 1
    mon_dicts = {1: deque()}
    mon_size = {1: 0}

    for _ in range(Q):
        mon_where = list(map(int, input().split()))
        batch(mon_where, mon_maps, num, mon_dicts, mon_size)
        num += 1
        # 배치 이후 맵 초기화
        mon_maps = [[0]*N for _ in range(N)]

        # size 순으로 정렬
        mon_size_item = sorted(mon_size.items(), key=lambda x:x[1], reverse=True)
        move(mon_maps, mon_size_item, mon_dicts, mon_size)
