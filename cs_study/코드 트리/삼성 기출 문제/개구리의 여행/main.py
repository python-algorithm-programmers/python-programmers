import heapq


# 점프해서 갈 수 있는 곳 기준
def jump(y, x, jump_stat, maps, N):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    result = []
    for dy, dx in directions:
        ny, nx = y, x
        blocked = False
        for step in range(1, jump_stat + 1):
            ny += dy
            nx += dx
            if not (0 <= ny < N and 0 <= nx < N):
                blocked = True
                break
            if maps[ny][nx] == '#':
                blocked = True
                break
        if not blocked and maps[ny][nx] == '.':
            result.append((ny, nx))
    return result

# 다익스트라: 항상 가장 짧은 거리로 확정 지어야함을 기억
# 그렇게 하기 위해 다음 가야될 위치를 heap으로 최단 거리만을 앞에 두는 형태로 구성
def solve(N, maps, start, end):
    sy, sx = start
    ey, ex = end
    INF = 10 ** 5
    dist = [[[INF] * 6 for _ in range(N)] for _ in range(N)]
    pq = []

    # 현재 개구리의 위치와 점프력에 따른 최소 비용 = turn을 dist로 표현
    # 즉, 지금의 jump_stat 상태로 도착했을 때의 turn 값
    dist[sy][sx][1] = 0
    heapq.heappush(pq, (0, sy, sx, 1))

    while pq:
        turn, y, x, jump_stat = heapq.heappop(pq)
        if (y, x) == (ey, ex):
            return turn

        if turn > dist[y][x][jump_stat]:
            continue

        # 점프해서 갈 수 있는 4방향 모두 점검하고 나온 결과물
        for ny, nx in jump(y, x, jump_stat, maps, N):
            next_turn = turn + 1
            if next_turn < dist[ny][nx][jump_stat]:
                dist[ny][nx][jump_stat] = next_turn
                heapq.heappush(pq, (next_turn, ny, nx, jump_stat))

        # 업그레이드
        if jump_stat < 5:
            next_jump = jump_stat + 1
            next_turn = turn + next_jump ** 2
            if next_turn < dist[y][x][next_jump]:
                dist[y][x][next_jump] = next_turn
                heapq.heappush(pq, (next_turn, y, x, next_jump))

        # 다운그레이드
        if jump_stat > 1:
            for next_jump in range(1, jump_stat):
                next_turn = turn + 1
                if next_turn < dist[y][x][next_jump]:
                    dist[y][x][next_jump] = next_turn
                    heapq.heappush(pq, (next_turn, y, x, next_jump))
    return -1

if __name__ == "__main__":
    N = int(input())
    maps = [list(input().strip()) for _ in range(N)]
    Q = int(input())
    for _ in range(Q):
        sy, sx, ey, ex = map(int, input().split())
        sy, sx, ey, ex = sy-1, sx-1, ey-1, ex-1
        answer = solve(N, maps, (sy,sx), (ey,ex))
        print(answer)