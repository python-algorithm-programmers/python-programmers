def solution(N, num_list):

    return

if __name__ == "__main__":
    import sys
    lines = sys.stdin.readlines()
    N = int(lines[0].strip())
    num_list = []
    for line in lines[1:]:
        num_list.append(list(map(int, line.split(" "))))
    print(solution(N, num_list))