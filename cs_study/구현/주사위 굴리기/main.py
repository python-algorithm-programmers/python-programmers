def rotate_dice(cur_dice, direction):
    """
    주사위 면을 배열의 인덱스로 고정
    0: 위
    1: 아래
    2: 북
    3: 남
    4: 서
    5: 동
    """

    # 동쪽이면
    """
    1. 동쪽으로 굴리면
    위 -> 동
    아래 -> 서
    서 -> 위
    동 -> 아래
    """
    if direction == 1:
        t_east = cur_dice[5]
        t_west = cur_dice[4]
        t_up = cur_dice[0]
        t_down = cur_dice[1]

        cur_dice[0] = t_west
        cur_dice[1] = t_east
        cur_dice[4] = t_down
        cur_dice[5] = t_up

    # 서쪽이면
        """
        2. 서쪽으로 굴리면
        위 -> 서
        아래 -> 동
        동 -> 위
        서 -> 아래
        """
    elif direction == 2:
        t_east = cur_dice[5]
        t_west = cur_dice[4]
        t_up = cur_dice[0]
        t_down = cur_dice[1]

        cur_dice[0] = t_east
        cur_dice[1] = t_west
        cur_dice[4] = t_up
        cur_dice[5] = t_down


    # 북쪽이면
        """
        3. 북쪽으로 굴리면
        위 -> 남
        아래 -> 북
        남 -> 아래
        북 -> 위
        
        
        """
    elif direction == 3:
        t_north = cur_dice[2]
        t_south = cur_dice[3]
        t_up = cur_dice[0]
        t_down = cur_dice[1]

        cur_dice[0] = t_south
        cur_dice[1] = t_north
        cur_dice[2] = t_up
        cur_dice[3] = t_down


    # 남쪽이면
        """
        4. 남쪽으로 굴리면
        위 -> 북
        아래 -> 남
        북 -> 아래
        남 -> 위
        """
    else:
        t_north = cur_dice[2]
        t_south = cur_dice[3]
        t_up = cur_dice[0]
        t_down = cur_dice[1]

        cur_dice[0] = t_north
        cur_dice[1] = t_south
        cur_dice[2] = t_down
        cur_dice[3] = t_up



def find_up(dice):
    return dice[0]

def change_dice_or_maps(dice, maps, rotate_loc):
    rotate_y, rotate_x = rotate_loc
    check_v = maps[rotate_y][rotate_x]
    if check_v == 0:
        maps[rotate_y][rotate_x] = dice[1]

    else:
        dice[1] = maps[rotate_y][rotate_x]
        maps[rotate_y][rotate_x] = 0

def solution(N, M, x, y, K, maps, comm) -> list[int]:
    result = []
    dice = [0, 0, 0, 0, 0, 0]
    directions = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]

    # 시작점 찾기
    cur_loc = [y, x]
    for command in comm:
        # maps에서 벗어낫는 지 확인
        #print()
        #print("command", directions[command])
        dy, dx = directions[command]
        cur_y, cur_x = cur_loc[0], cur_loc[1]
        ny, nx = cur_y+dy, cur_x+dx
        #print("cur_loc", cur_loc)
        #print("cur_dice", dice)

        if 0 <= ny < N and 0 <= nx < M:
            rotate_dice(dice, command)
            change_dice_or_maps(dice, maps, [ny, nx])
            #print("rotate_dice", dice)
            result.append(find_up(dice))
            cur_loc = [ny, nx]

    return result


if __name__ == "__main__":
    N, M, y, x, K = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))

    comm = list(map(int, input().split()))
    result = solution(N, M, x, y, K, maps, comm)
    for i in range(len(result)):
        print(result[i])