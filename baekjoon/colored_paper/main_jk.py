def dfs(x, y , N, num_list, white_cnt, blue_cnt):
    # 종료조건: 모든 정사각형이 같은 색인 경우
    initial_color = num_list[0][0]
    all_same = True
    for i in range(x, x+N):
        for j in range(y, y+N):
            if num_list[x][y] != initial_color:
                all_same = False
                break
        if not all_same:
            break

    if all_same:
        if initial_color == 1:
            blue_cnt[0] += 1
        else:
            white_cnt[0] += 1
        return

    # 4개의 사분면 분배
    half = N // 2
    dfs(x, y, half, num_list, white_cnt, blue_cnt)
    dfs(x+half, y, half, num_list, white_cnt, blue_cnt)
    dfs(x, y+half, half, num_list, white_cnt, blue_cnt)
    dfs(x+half, y+half, half, num_list, white_cnt, blue_cnt)

def solution(N, num_list):
    white_cnt = [0]
    blue_cnt = [0]
    dfs(0, 0, N, num_list, white_cnt, blue_cnt)
    return white_cnt[0], blue_cnt[0]


if __name__ == '__main__':
    import sys
    lines = sys.stdin.readlines()
    num_list = []
    N = int(lines[0])
    for line in lines[1:]:
        new_line = line.strip().split(' ')
        int_line = list(map(int, new_line))
        num_list.append(int_line)

    white_cnt, blue_cnt = solution(N, num_list)
    print(white_cnt)
    print(blue_cnt)
