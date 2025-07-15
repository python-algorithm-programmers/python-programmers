def dfs(idx, cnt, N, visited, total):
    # N개 놓는 경우
    if cnt == N:
        total[0] += 1
        return

    # 인덱스 다 돈 경우
    if idx == N:
        return

    # idx를 행 단위로 생각
    y = idx

    # 놓을 자리가 없는 경우도 고려해서 안되면 인덱스 늘려서 다음 자리로 이동시켜야됨
    place_on = False

    # 놓을 수 있는 지 이전 퀸의 여파를 확인
    # 왼쪽 위에서 아래로 내려갈 것이고
    # 행 단위로 돌면서 그 행에 해당하는 x,열을 접근하는 식으로 생각
    for x in range(N):
        if not visited[y][x]:
            go_ok = True

            # 위아래 열 안에 퀸있는 지 검토
            for row in range(N):
                if visited[row][x]:
                    go_ok = False
                    break

            # 왼쪽 위 대각선 검토
            if go_ok:
                # 변수를 따로 지정해서 위쪽 대각선 라인에 있는 퀸 조사
                r, c = y, x
                while r>=0 and c>=0:
                    if visited[r][c]:
                        go_ok = False
                        break
                    r -= 1
                    c -= 1

            # 오른쪽 위 대각선 검토
            if go_ok:
                r, c = y, x
                while r>=0 and c<N:
                    if visited[r][c]:
                        go_ok = False
                        break
                    r -= 1
                    c += 1

            # 놓을 수 있는 지 확정이 되면 놓고 참조변수 백트래킹
            if go_ok:
                place_on = True
                visited[y][x] = True
                dfs(idx+1, cnt+1, N, visited, total)
                visited[y][x] = False

    if not place_on:
        dfs(idx+1, cnt, N, visited, total)

def solution(N, visited):
    total = [0]
    dfs(0, 0, N, visited, total)
    return total[0]

if __name__ == "__main__":
    N = int(input())
    visited = [[False]*N for _ in range(N)]
    print(solution(N, visited))