import sys


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
    variants = []

    # 정자세 + 한 군데 3회전, 좌,우 뒤집고 3회전 -> 16개
    # 좌표로 모두 바꿔서 저장
    for block in blocks:
        # 정자세 추가
        variants.append(mapper(block))

        # 깊은 복사
        rotate_block = block
        for _ in range(3):
            # 회전시 고려
            rotate_block = rotate(rotate_block)
            variants.append(mapper(rotate_block))

            # 그 이후 y,x 뒤집기
            flip_y_block = flip_y(rotate_block)
            variants.append(mapper(flip_y_block))
            flip_x_block = flip_x(rotate_block)
            variants.append(mapper(flip_x_block))

    # 최댓값 찾기
    for i in range(N):
        for j in range(M):
            for variant in variants:
                block_sum = 0
                add_flag = True
                for block_y, block_x in variant:
                    if 0 <= block_y + i < N and 0 <= block_x + j < M:
                        block_sum += maps[block_y + i][block_x + j]
                    else:
                        add_flag = False
                        break

                if not add_flag:
                    continue

                if block_sum > best_sum:
                    best_sum = block_sum

    return best_sum


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, sys.stdin.readline().strip().split())))
    print(solution(N,M,maps))