from pprint import pprint

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_arr = list(map(list, zip(*[row[::-1] for row in arr])))

grav_arr = [[1, 1, 1], [0, 0, 2], [0, 2, 0], [3, 0, 3]]
pprint(grav_arr)
N, M = 4, 3
for c in range(M):
    stack = []
    for r in range(N):
        if grav_arr[r][c] != 0:
            stack.append(grav_arr[r][c])

    # 아래부터 채우고, 남은 빈칸을 0으로 만들기
    # r_idx -> 빈칸 수를 의미
    # stack에는 차례대로 쌓여있어
    # stack 털고 비면 r_idx만큼 넣어주면 되는 데, 인덱스를 모름
    for r in range(N-1, -1, -1):
        if stack:
            add = stack.pop()
            grav_arr[r][c] = add
        else:
            grav_arr[r][c] = 0

pprint(grav_arr)



