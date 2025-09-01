def mapper(block):
    block_cod = []
    for y in range(len(block)):
        for x in range(len(block[0])):
            if block[y][x] == 1:
                block_cod.append((y,x))
    return block_cod

def rotate(arr):
    return [col for col in zip(*arr[::-1])]

def flip_y(arr):
    return [col[::-1] for col in arr]

def flip_x(arr):
    return arr[::-1]
def solution(N,M,maps):
    best_sum = 0
    block1 = [[1,1,1,1]]
    block2 = [[1,1],[1,1]]
    block3 = [[1, 0], [1, 0], [1, 1]]
    block4 = [[1,0], [1, 1], [0,1]]
    block5 = [[1,1,1],[0,1,0]]
    blocks = [block1, block2, block3, block4, block5]

    for block in blocks:
        for i in range(N):
            for j in range(M):
                # 기본
                default_block_coord = mapper(block)
                add_flag = True
                block_sum = 0
                for block_y, block_x in default_block_coord:
                    if 0<=block_y+i<N and 0<=block_x+j<M:
                        block_sum += maps[block_y+i][block_x+j]
                    else:
                        add_flag = False
                        break

                if not add_flag:
                    block_sum = 0

                # print("default_block_coord")
                # print((i,j),default_block_coord)
                # print(block_sum)
                # print()
                best_sum = max(best_sum, block_sum)

                # 3회전
                rotate_block = block
                for _ in range(3):
                    block_sum = 0
                    add_flag = True

                    rotate_block = rotate(rotate_block)
                    rotate_coord = mapper(rotate_block)

                    for block_y, block_x in rotate_coord:
                        if 0 <= block_y + i < N and 0 <= block_x + j < M:
                            block_sum += maps[block_y + i][block_x + j]
                        else:
                            add_flag = False
                            break

                    if not add_flag:
                        continue

                    # print("rotate_coord")
                    # print((i, j), rotate_coord)
                    # print(block_sum)
                    # print()
                    best_sum = max(best_sum, block_sum)

                # 축반전 3번
                flip_y_block = flip_y(block)
                flip_x_block = flip_x(block)
                flip_y_x_block = flip_y(flip_x_block)
                flip_y_block_coord = mapper(flip_y_block)
                flip_x_block_coord = mapper(flip_x_block)
                flip_y_x_block_coord = mapper(flip_y_x_block)
                flip_coords = [flip_y_block_coord, flip_x_block_coord, flip_y_x_block_coord]
                for flip_block_coord in flip_coords:
                    add_flag = True
                    block_sum = 0
                    for block_y, block_x in flip_block_coord:
                        if 0 <= block_y + i < N and 0 <= block_x + j < M:
                            block_sum += maps[block_y + i][block_x + j]
                        else:
                            add_flag = False
                            break

                    if not add_flag:
                        continue

                    # print("flip_block_coord")
                    # print((i, j), flip_block_coord)
                    # print(block_sum)
                    # print()
                    best_sum = max(best_sum, block_sum)

    return best_sum


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().strip().split())))
    print(solution(N,M,maps))