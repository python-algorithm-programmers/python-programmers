# 문제 정의
# 0. 있는 위치에 visited true로
# 1. 4방향 중에 청소 여부 확인, 이때 몸방향도 기억
    # 없다면, 방향 유지한 채로 뒤로 후진
        # 뒤에 벽이 있으면, 종료
        # 벽이 없다면, 뒤로 한칸 이동 이때 몸방향은 유지
# 2. # 있다면,
        # 반시계 방향으로 90도 몸방향 회전
        # 청소되지 않은 칸이 몸방향에 걸리면 전진

# 참고사항: 북 동 남 서 순으로 0~3까지 몸방향을 둔다
# 멈추는 조건: 청소할 영역이 없다, 벽을 뒤에 등졌다

from collections import deque
def bfs(N, M, y, x, body_pos, maps, visited):
    clean_cnt = 0
    queue = deque([(y, x, body_pos)])
    while queue:
        # 현재 위치 닦기
        cur_y, cur_x, cur_pos = queue.popleft()
        visited[cur_y][cur_x] = True
        clean_cnt += 1
        find_flag = False

        # 방향 확인, 반시계 90도 방향으로 돌리면서 한칸 앞에 있는 지만 확인
        directions = [(-1, 0, 0), (0, -1, 3), (1, 0, 2), (0, 1, 1)]

        # 현재 방향 기준에서 90도 돌린 방향을 찾아야함
        for __ in range(len(directions)):
            new_pos = (cur_pos+3) % 4
            dy, dx, __ = [dir for dir in directions if dir[2] == new_pos][0]
            ny, nx = cur_y+dy, cur_x+dx

            # 4방향 중 간본 거에 빈공간이 있으면 + 벽이 아니면
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and maps[ny][nx]==0:
                # 몸방향 바꾸고 전진
                queue.append((ny, nx, new_pos))

                # 후진 로직 안타기
                find_flag = True
                break

        # 4방향 중에 못 찾으면 한칸 뒤 확인
        if not find_flag:
            # 몸방향의 뒤 방향에만 벽이 있는 지 확인
            back_y, back_x, cur_pos = [dir for dir in directions if dir[2] == cur_pos][0]

            # 몸방향 뒤 확인
            by, bx = cur_y+back_y, cur_x+back_x

            # 벽이 존재
            if maps[by][bx] == 1:
                break

            # 벽이 아니라면
            else:
                queue.append((by, bx, cur_pos))

    return clean_cnt



def solution(map_len, start, maps):
    n, m = map_len[0], map_len[1]
    y, x, body_pos = start[0], start[1], start[2]

    # 방문 위치 확인
    visited = [[False]*m for __ in range(n)]

    clean_cnt = bfs(n, m, y, x, body_pos, maps, visited)
    return clean_cnt

if __name__ == "__main__":
    import sys
    map_len = list(map(int, sys.stdin.readline().strip().split(" ")))
    start = list(map(int, sys.stdin.readline().strip().split(" ")))

    # 맵 저장
    # lines = sys.stdin.readlines()
    # maps = [list(map(int, line.strip().split(" "))) for line in lines]
    maps = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 0, 0, 1, 1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    print(solution(map_len, start, maps))

