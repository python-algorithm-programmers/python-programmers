from collections import deque
def solution(N, M, maps):
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    chain_cnt = 0

    while True:
        # bfs로 연결된 것들 모두 찾기
        visited = [[False]*M for _ in range(N)]
        delete_graph = []
        for y in range(N):
            for x in range(M):
                if visited[y][x] or maps[y][x] == '.':
                    continue

                # 탐색이 안된 지점만 찾는 것으로
                graph_q = deque()
                graph_q.append((y,x))
                puyo_graph_list = [(y,x)]
                color = maps[y][x]
                while graph_q:
                    start_y, start_x = graph_q.popleft()
                    visited[start_y][start_x] = True

                    for dy, dx in directions:
                        ny, nx = start_y+dy, start_x+dx
                        if 0<=ny<N and 0<=nx<M and not visited[ny][nx] \
                            and maps[ny][nx] == color:
                            puyo_graph_list.append((ny, nx))
                            graph_q.append((ny, nx))
                            visited[ny][nx] = True

                if len(puyo_graph_list) >= 4:
                    delete_graph.extend(puyo_graph_list)

        # 제거할 대상이 없으면 끝난 것
        if not delete_graph:
            return chain_cnt

        # 원소 제거
        for delete_y, delete_x in delete_graph:
            maps[delete_y][delete_x] = "."

        # 중력 적용, 열 우선 적용
        for x in range(M):
            hallow_list = []
            for y in range(N-1,-1,-1):
                if maps[y][x] != '.' and hallow_list:
                    hallow_y, hallow_x = hallow_list.pop(0)
                    maps[hallow_y][hallow_x] = maps[y][x]
                    hallow_list.append((y,x))
                    maps[y][x] = '.'
                elif maps[y][x] == '.':
                    hallow_list.append((y,x))

        # 턴 수 증가
        chain_cnt += 1

if __name__ == "__main__":
    N, M = 12, 6
    maps = []
    for _ in range(N):
        maps.append(list(input()))
    print(solution(N, M, maps))
