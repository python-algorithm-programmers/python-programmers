
def solution(N, maps):
    for i in range(N):
        result = [str(i) for _ in range(N)]
        print(" ".join(result))

if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline().strip())
    lines = sys.stdin.readlines()

    # maps
    maps = [list(map(int, line.strip().split(" "))) for line in lines]
    solution(N, maps)
