from collections import deque

# dfs vs for 문으로 이제 고려
def dfs(N, start, middle, dest, turn_info, maps):
    if N == 0:
        return

    # 맨처음 원소까지 내려온다음에 옮김
    # 디테일은 교차로 내려와야 된다는 것임
    dfs(N-1, start, dest, middle, turn_info, maps)

    # a[n+1] = 2a[n]+1
    # a[n] = 2^n-1
    last_n = maps[start].pop(0)
    maps[dest].insert(0, last_n)
    turn_info.append((start, dest))

    # 1번째 꺼는 옮겼으니 더 이상 움직이지 않고 리턴되고
    # 2번째 꺼를 이어서 옮기고
    # 다시 1번째 꺼를 그 위로 옮겨서 가는 식으로 구성해야함
    dfs(N-1, middle, start, dest, turn_info, maps)


def solution(N):
    turn_info = []
    maps = [[] for _ in range(4)]
    for i in range(N):
        maps[1].append(i+1)
    dfs(N, 1, 2, 3, turn_info, maps)
    print(2**N-1)
    for start, end in turn_info:
        print(f"{start} {end}")

if __name__ == "__main__":
    N = int(input())
    solution(N)