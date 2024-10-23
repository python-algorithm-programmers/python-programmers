def dfs(N, M, num_list):
    # 종료 조건
    if len(num_list) == M:
        print(" ".join((map(str, num_list))))
        return


    for i in range(1, N+1):
        # 중복 없이 적용하기 위해
        if i not in num_list:
            dfs(N, M, num_list+[i])


def solution(N, M):
    dfs(N, M, [])



if __name__ == "__main__":
    import sys
    lines = sys.stdin.readlines()
    N, M = lines[0].strip().split(" ")
    solution(int(N), int(M))