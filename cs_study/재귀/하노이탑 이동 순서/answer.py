import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(n, src, dst, aux, maps, turn_info):
    """
    n개의 원판을 src 기둥에서 dst 기둥으로 옮길 때,
    aux 기둥을 보조로 쓰는 재귀 구현.
    maps: [[], peg1_list, peg2_list, peg3_list]
    turn_info: 이동 기록을 (from, to) 튜플로 append
    """
    if n == 0:
        return

    # 1) 맨 위 n-1개를 src -> aux 로
    dfs(n-1, src, aux, dst, maps, turn_info)

    # 2) 남은 한 개를 src -> dst 로
    disk = maps[src].pop(0)
    maps[dst].insert(0, disk)
    turn_info.append((src, dst))

    # 3) aux 에 쌓아둔 n-1개를 aux -> dst 로
    dfs(n-1, aux, dst, src, maps, turn_info)

def solution(N):
    # maps[1]에 1부터 N까지 차곡차곡 쌓습니다
    maps = [None, list(range(1, N+1)), [], []]
    turn_info = []

    # 1번 기둥 → 3번 기둥, 보조는 2번
    dfs(N, 1, 3, 2, maps, turn_info)

    # 결과 출력
    print(len(turn_info))
    print("\n".join(f"{a} {b}" for a, b in turn_info))

if __name__ == "__main__":
    N = int(input())
    solution(N)