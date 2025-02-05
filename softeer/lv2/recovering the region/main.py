# 구역을 어떻게 나눌 것인가?

def solution(N, maps):
    return

if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline().strip())
    lines = sys.stdin.readlines()

    # maps
    maps = [list(map(int, line.strip().split(" "))) for line in lines]
    print(solution(N, maps))
