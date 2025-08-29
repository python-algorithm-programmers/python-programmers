from collections import deque

def solution(N, M, puyo_maps):
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    chain_cnt = 0

    while True:
        visited = [[False]*N for _ in range(M)]
        remove_blocks = []

        # 보드 전체 탐색
        for y in range(M):
            for x in range(N):
                if puyo_maps[y][x] == '.' or visited[y][x]:
                    continue

                color = puyo_maps[y][x]
                graph_q = deque()
                graph_q.append((y,x))
                visited[y][x] = True
                puyo_graph_list = [(y,x)]

                while graph_q:
                    cy, cx = graph_q.popleft()
                    for dy, dx in directions:
                        ny, nx = cy+dy, cx+dx
                        if 0 <= ny < M and 0 <= nx < N and not visited[ny][nx] \
                                and puyo_maps[ny][nx] == color:
                            visited[ny][nx] = True
                            graph_q.append((ny,nx))
                            puyo_graph_list.append((ny,nx))

                if len(puyo_graph_list) >= 4:
                    remove_blocks.extend(puyo_graph_list)

        # 지울 뿌요 없으면 종료
        if not remove_blocks:
            break

        # 지우기
        for ry, rx in remove_blocks:
            puyo_maps[ry][rx] = '.'

        # 중력 처리 (열 단위)
        for x in range(N):
            stack = []
            for y in range(M-1, -1, -1):  # 아래쪽부터 위로
                if puyo_maps[y][x] != '.':
                    stack.append(puyo_maps[y][x])
            for y in range(M-1, -1, -1):
                if stack:
                    puyo_maps[y][x] = stack.pop(0)
                else:
                    puyo_maps[y][x] = '.'

        chain_cnt += 1

    return chain_cnt


if __name__ == "__main__":
    M, N = 12, 6   # 고정 크기
    puyo_maps = [list(input().strip()) for _ in range(M)]
    print(solution(N, M, puyo_maps))