def solution(m, n, board):
    board_flag = [[False]*n for __ in range(m)]
    while_flag = True
    result = 0
    while while_flag:
        cnt = 0
        for y, row in enumerate(board):
            for x, block in enumerate(row):
                # 4방향 탐색 (동쪽부터)
                directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
                for i in range(0, len(directions), 2):
                    # 3연속으로 존재할 때만 찾기
                    consecutive_cnt = 0
                    block_index_list = []

                    for j in range(3):
                        index = i+j
                        if index > len(directions) - 1:
                            index -= len(directions)
                        dy, dx = directions[index][0], directions[index][1]
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < len(board) and 0 <= nx < len(row):
                            if board[ny][nx] == block:
                                consecutive_cnt += 1
                                block_index_list.append((ny, nx))

                            if consecutive_cnt == 3:
                                for post_y, post_x in block_index_list:
                                    board_flag[post_y][post_x] = True

        # 탐색 끝나고 flag 지정이 완료되었음
        for y in range(len(board)):
            for x in range(len(board[y])-1, -1, -1):
                if board_flag[y][x] == True:
                    del board_flag[y][x]
                    board[y] = board[y][:x]+board[y][x+1:]
                    cnt += 1

        result += cnt

        # 한개의 block도 삭제하지 못하면 끝
        if cnt == 0:
            break

    return result


if __name__ == "__main__":
    m,n = 4,5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    print(solution(m, n, board))