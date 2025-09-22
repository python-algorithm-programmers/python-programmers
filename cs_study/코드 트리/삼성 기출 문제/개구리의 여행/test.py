# jump해서 갈 수 있는 범위 확인
def jump(N, maps, start_p, jump_stat):
    result = []
    directions = [(-1,0), (1, 0), (0, 1), (0, -1)]
    start_y, start_x = start_p
    for dy, dx in directions:
        # 지나가는 곳에 천적 있을 수도 있으니 분할해서 범위 계산
        ny, nx = start_y, start_x
        break_flag = False

        for i in range(1, jump_stat+1):
            ny += dy
            nx += dx

            if not (0 <= ny < N and 0 <= nx < N):
                break_flag = True
                break

            if maps[ny][nx] == "#":
                break_flag = True
                break

        # 도중에 문제가 될만한 곳이 없고 안전한 곳인 경우에만 등록
        if not break_flag and maps[ny][nx] == ".":
            result.append((ny, nx))

    return result

def solution(start_p, end_p, N, maps):
    INF = 10 ** 5
    start_y, start_x = start_p
    ey, ex = end_p
    dist = [[[INF] * 6 for _ in range(N)] for _ in range(N)]
    dist[start_y][start_x][1] = 0
    pq = []
    heapq.heappush(pq, (0, start_y, start_x, 1))
    while pq:
        turn, y, x, jump_stat = heapq.heappop(pq)

        # 종료 조건
        if ey == y and ex == x:
            return turn

        # 최소만 dp로써 기록되도록 해야하니
        if turn > dist[y][x][jump_stat]:
            continue

        # 최소 거리인 것을 확정짓는 범위 내에서 결정
        # 점프 확인
        for ny, nx in jump(N, maps, (y, x), jump_stat):
            next_turn = turn + 1
            if dist[ny][nx][jump_stat] > next_turn:
                dist[ny][nx][jump_stat] = next_turn
                heapq.heappush(pq, (next_turn, ny, nx, jump_stat))

        # 업그레이드
        if jump_stat < 5:
            jump_stat += 1
            next_turn = turn + jump_stat ** 2
            if dist[y][x][jump_stat] > next_turn:
                dist[y][x][jump_stat] = next_turn
                heapq.heappush(pq, (next_turn, y, x, jump_stat))

        # 다운그레이드
        if 1 < jump_stat:
            for slow_jump_stat in range(1, jump_stat):
                next_turn = turn + 1
                if dist[y][x][slow_jump_stat] > next_turn:
                    dist[y][x][slow_jump_stat] = next_turn
                    heapq.heappush(pq, (next_turn, y, x, slow_jump_stat))

    return -1





if __name__ == "__main__":
    import heapq
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(input().strip()))

    Q = int(input())
    for _ in range(Q):
        sy, sx, ey, ex = map(int, input().split())
        start_y, start_x, end_y, end_x = sy-1, sx-1, ey-1, ex-1
        print(solution((start_y, start_x), (end_y, end_x), N, maps))
