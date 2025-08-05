import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(r, c, idx, N, directions, dest_y, dest_x, close_flag, answer):
    # 1) 이미 찾았다면 바로 종료
    if close_flag[0]:
        return

    # 2) 2×2 블록 기준 단계
    if N == 1:
        for dy, dx in directions:
            go_y, go_x = r + dy, c + dx
            if go_y == dest_y and go_x == dest_x:
                close_flag[0] = True
                answer[0] = idx[0]
                return
            idx[0] += 1
        return

    # 3) 사분면 크기와 한 사분면의 칸 수
    half = 2 ** (N - 1)
    block_size = half * half

    # 4) 네 사분면 순회: (0,0), (0,half), (half,0), (half,half)
    for dr, dc in ((0,0), (0,half), (half,0), (half,half)):
        nr, nc = r + dr, c + dc

        # 4-1) 목적지가 이 사분면 안에 있으면 재귀 진입
        if nr <= dest_y < nr + half and nc <= dest_x < nc + half:
            dfs(nr, nc, idx, N-1, directions, dest_y, dest_x, close_flag, answer)
            return

        # 4-2) 아니면, 이 사분면 전체를 스킵—인덱스만 증가
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