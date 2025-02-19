def dfs(mine, turn, popularity, best, input_data, N):
    # 종료 조건
    if turn == N:
        best[0] = max(best[0], popularity)
        return

    # 현재 유명인
    popular, familiar = input_data[turn]

    if abs(popular - mine) <= familiar:
        dfs(mine+1, turn+1, popularity+1, best, input_data, N)

    # 건너뛰기
    dfs(mine, turn+1, popularity, best, input_data, N)

def solution(N, input_data):
    mine = 0
    best = [0]
    dfs(mine, 0, 0, best, input_data, N)
    return best[0]

if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline().strip())
    input_data = []
    for __ in range(N):
        input_list = list(map(int, sys.stdin.readline().strip().split(" ")))
        popular, familiar = input_list[0], input_list[1]
        input_data.append((popular, familiar))

    print(solution(N, input_data))