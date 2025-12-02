"""
0 흰색
1 빨간색
2 파란색

"""
from pprint import pprint
def solution(N, K, chess_map, horse_info, horse_map):
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    turn = 0
    end_flag = [False]

    def move_white(horse_idx, start, end):
        r, c = start
        ny, nx = end

        # 위의 있는 말 포함해서 위에 쌓기
        horse_top = horse_map[r][c].index(horse_idx)
        move_horses = horse_map[r][c][horse_top:]
        horse_map[ny][nx].extend(move_horses)

        # 만약 위에 쌓았을 때, 사이즈가 4이상이면
        if len(horse_map[ny][nx]) >= 4:
            end_flag[0] = True

        # 옮기고 난 후에는 기존 map 에서 삭제
        horse_map[r][c] = horse_map[r][c][:horse_top]

        # 그에 해당하는 말들 위치 바꿔주기
        for renew_h in move_horses:
            horse_info[renew_h][0] = ny
            horse_info[renew_h][1] = nx

    def move_red(horse_idx, start, end):
        r, c = start
        ny, nx = end

        # 위의 있는 말 포함해서 위에 쌓기
        horse_top = horse_map[r][c].index(horse_idx)
        move_horses = horse_map[r][c][horse_top:]

        # 뒤집고 삽입
        move_horses.reverse()
        horse_map[ny][nx].extend(move_horses)

        # 만약 위에 쌓았을 때, 사이즈가 4이상이면
        if len(horse_map[ny][nx]) >= 4:
            end_flag[0] = True

        # 옮기고 난 후에는 기존 map 에서 삭제
        horse_map[r][c] = horse_map[r][c][:horse_top]

        # 그에 해당하는 말들 위치 바꿔주기
        for renew_h in move_horses:
            horse_info[renew_h][0] = ny
            horse_info[renew_h][1] = nx

    def move_blue(horse_idx, start, h_d):
        r, c = start
        if h_d >= 2:
            h_d = 5 - h_d
        else:
            h_d = 1 - h_d

        # 바꾼 방향으로 다시 계산
        dy, dx = directions[h_d]
        my, mx = r + dy, c + dx

        # 방향은 바꿔줘야지
        horse_info[horse_idx][2] = h_d

        # 경계면 안인 경우
        if 0 <= my < N and 0 <= mx < N:
            # 흰색인 경우
            if chess_map[my][mx] == 0:
                move_white(horse_idx, (r, c), (my, mx))


            # 빨간색인 경우
            elif chess_map[my][mx] == 1:
                move_red(horse_idx, (r, c), (my, mx))

            # 파란색인 경우
            else:
                pass

        # 경계면 밖인 경우
        else:
            pass

    while True:
        if turn > 1000:
            return -1

        turn += 1
        horse_key = list(horse_info.keys())
        horse_key.sort()

        """
        말 이동
        """
        #print("turn", turn)
        #pprint(horse_map)
        #print(horse_info)
        #pprint(chess_map)

        for horse_idx in horse_key:
            h_r, h_c, h_d = horse_info[horse_idx]
            dy, dx = directions[h_d]
            ny, nx = h_r+dy, h_c+dx

            # 경계면 안인 경우
            if 0 <= ny < N and 0 <= nx < N:
                # 흰색인 경우
                if chess_map[ny][nx] == 0:
                    flag = move_white(horse_idx, (h_r, h_c), (ny, nx))
                    if flag:
                        return turn

                # 빨간색인 경우
                elif chess_map[ny][nx] == 1:
                    flag = move_red(horse_idx, (h_r, h_c), (ny, nx))
                    if flag:
                        return turn

                # 파란색인 경우
                else:
                    move_blue(horse_idx, (h_r, h_c), h_d)

            # 경계면 밖인 경우
            else:
                move_blue(horse_idx, (h_r, h_c), h_d)

        if end_flag[0] == True:
            break
            #print("horse_idx", horse_idx)
            #pprint(horse_map)
            #print(horse_info)
            #pprint(chess_map)

    return turn


if __name__ == "__main__":
    N, K = map(int, input().split())
    chess_map = []
    horse_info = {}
    horse_map = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(N):
        chess_map.append(list(map(int, input().split())))

    for i in range(K):
        r, c, d = map(int, input().split())
        horse_info[i] = [r-1, c-1, d-1]
        horse_map[r-1][c-1].append(i)

    print(solution(N, K, chess_map, horse_info, horse_map))