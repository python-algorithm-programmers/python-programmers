def dfs(index, present, best, total, visited, maps):
    # 종료 조건
    if present == total:
        best[0] = max(present, best[0])
        return

    # index를 나눠서 현재 좌표 변환
    y = index // M
    x = index % N

    # 익었는 지 여부 확인
    if visited[y][x] == True:
        dfs(index+1, 0, best, total, visited, maps)
    else:
        # 일단 그 자리는 익어야함
        visited[y][x] = True

        # 인접한 방향이 모두 익은 경우, 상하좌우 순
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dy, dx in directions:
            ny, nx = y+dy, x+dx
            # 4방향 중에 안 익은 곳이 있을 때
            if 0 <= ny < M and 0 <= nx <N and not visited[ny][nx]:
                dfs(index, present+1, best, total, visited, maps)

                # 백트랙킹: 익음 해제, 에코 궁
                visited[y][x] = False
                visited[ny][nx] = False

        # 4방향 중에 안익은 곳이 없을 때, 종료
        return



def solution(M, N, maps):
    visited = [[False]*N for __ in range(M)]
    best = [0] # 값을 참조하기 때문
    total = 0
    for map in maps:
        for tomato in map:
            if tomato == 0:
                total += 1
    dfs(0, 0, best, total, visited, maps)
    return best[0]

if __name__ == "__main__":
    import sys
    M, N = list(map(int, sys.stdin.readline().split(" ")))
    lines = sys.stdin.readlines()
    maps = []
    for line in lines:
        maps.append(list(map(int, line.split(" "))))
    print(solution(M, N, maps))