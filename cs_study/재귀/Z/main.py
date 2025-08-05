def dfs(r, c, idx, N, directions, dest_y, dest_x, close_flag, answer):
    # 완전히 종료시키기
    if close_flag[0]:
        return

    # 2 by 2 적용
    if N == 1:
        for dy, dx in directions:
            go_y, go_x = r + dy, c + dx
            if go_y == dest_y and go_x == dest_x:
                close_flag[0] = True
                answer[0] = idx[0]
                return

            idx[0] += 1
        return

    next_step = 2**(N-1)
    dfs(r, c, idx, N-1, directions, dest_y, dest_x, close_flag, answer)
    dfs(r, c + next_step, idx, N-1, directions, dest_y, dest_x, close_flag, answer)
    dfs(r + next_step, c, idx, N-1, directions, dest_y, dest_x, close_flag, answer)
    dfs(r + next_step, c + next_step, idx, N-1, directions, dest_y, dest_x, close_flag, answer)

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