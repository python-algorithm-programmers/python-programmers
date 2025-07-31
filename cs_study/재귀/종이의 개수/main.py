def dfs(r, c, N, maps, cnt_dict):
    # 다른 원소가 있는 지 확인
    not_eq_flag = False
    y_list = [r+i for i in range(N)]
    x_list = [c+i for i in range(N)]
    past = maps[r][c]
    for y in y_list:
        for x in x_list:
            cur = maps[y][x]
            if cur != past:
                not_eq_flag = True
                break
            past = cur

        if not_eq_flag:
            break

    if not not_eq_flag:
        cnt_dict[past] = cnt_dict.get(past)+1
        return

    # 윗줄부터
    dfs(r, c, N // 3, maps, cnt_dict)
    dfs(r, c + N // 3, N // 3, maps, cnt_dict)
    dfs(r, c + 2*(N // 3), N // 3, maps, cnt_dict)

    dfs(r + N // 3, c, N // 3, maps, cnt_dict)
    dfs(r + N // 3, c + N // 3, N // 3, maps, cnt_dict)
    dfs(r + N // 3, c + 2*(N // 3), N // 3, maps, cnt_dict)

    dfs(r + 2*(N // 3), c, N // 3, maps, cnt_dict)
    dfs(r + 2*(N // 3), c + N // 3, N // 3, maps, cnt_dict)
    dfs(r + 2*(N // 3), c + 2*(N // 3), N // 3, maps, cnt_dict)


if __name__ == "__main__":
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    cnt_dict = {i: 0 for i in [-1, 0, 1]}
    dfs(0, 0, N, maps, cnt_dict)
    result = [v for k,v in cnt_dict.items()]
    for v in result:
        print(v)