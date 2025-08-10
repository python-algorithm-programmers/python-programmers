def rotate(sticker, sticker_row, sticker_col):
    # 시계 방향으로 회전
    rotate_sticker = [[0] * sticker_row for _ in range(sticker_col)]
    for i in range(sticker_col):
        for j in range(sticker_row):
            rotate_sticker[i][j] = sticker[sticker_row - 1 - j][i]
    return rotate_sticker, sticker_col, sticker_row
def solution(sticker_dict, N, M, K):
    note = [[0]*M for _ in range(N)]
    for _, sticker_list in sticker_dict.items():
        sr, sc = sticker_list[0]
        sticker = sticker_list[1:]
        rotate_cnt = 0

        while rotate_cnt < 4:
            end_flag = False

            # 위 -> 아래 이동
            for row_cnt in range(N-sr+1):
                # 왼 -> 우 이동
                for col_cnt in range(M-sc+1):
                    next_flag = False

                    # 탐색 시작
                    for r in range(sr):
                        for c in range(sc):
                            # print(N, M)
                            # print(r+row_cnt, c+col_cnt)
                            # print(sr, sc)
                            # print()
                            if sticker[r][c] == 1 and note[r+row_cnt][c+col_cnt] == 1:
                                next_flag = True
                            if next_flag:
                                break
                        if next_flag:
                            break

                    if not next_flag:
                        end_flag = True
                        # 스티커 넣기
                        for y in range(sr):
                            for x in range(sc):
                                if sticker[y][x] == 1:
                                    note[y+row_cnt][x+col_cnt] = 1
                    if end_flag:
                        break

                if end_flag:
                    break

            if end_flag:
                break

            # 회전 후 바꾸기
            new_sticker, new_sr, new_sc = rotate(sticker, sr, sc)
            sticker, sr, sc = new_sticker, new_sr, new_sc
            rotate_cnt += 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if note[i][j] == 1:
                answer += 1
    return answer



if __name__ == "__main__":
    N, M, K = map(int, input().split())
    sticker_dict = {}
    for i in range(K):
        sticker_row, sticker_col = map(int, input().split())
        for _ in range(sticker_row):
            if not sticker_dict.get(i):
                sticker_dict[i] = [[sticker_row, sticker_col]]

            sticker_dict[i].append(list(map(int, input().split())))
    print(solution(sticker_dict, N, M, K))