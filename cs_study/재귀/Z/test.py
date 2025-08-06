def dfs (r, c, idx, N, directions, dest_y, dest_x, close_flag, answer):
    # 1) 이미 찾았다면 바로 종료
    if close_flag[0]:
        return

    # 2) 2×2 블록 기준 단계
    if N == 1:
        for dy, dx in directions:
            go_y, go_x = r + dy, c + dx
            # 찾았으면 바로 복귀
            if go_y == dest_y and go_x == dest_x:
                close_flag[0] = True
                answer[0] = idx[0]
                return
            idx[0] += 1
        return

    # 3) 필요한 부분만 백트래킹으로 찾기
    half = 2 ** (N-1)
    block_size = half * half
    half_directions = [(0,0), (0,half), (half,0), (half,half)]

    # 찾으면 그쪽으로 진입
    for ny, nx in half_directions:
        if ny<=dest_y<ny+half and nx<=dest_x<nx+half:
            dfs(ny, nx, idx, N-1, directions, dest_y, dest_x, close_flag, answer)

        # 못 찾으면 다음번으로 이동
        idx[0] += block_size

def solution(N, dest_y, dest_x):
    close_flag = [False]
    idx = [0]
    answer = [0]
    directions = [(0,0),(0,1),(1,0),(1,1)]
    dfs(0, 0, idx, N, directions, dest_y, dest_x, close_flag, answer)
    return answer[0]

if __name__ == "__main__":
    N, dest_y, dest_x = map(int, input().split())
    print(solution(N, dest_y, dest_x))