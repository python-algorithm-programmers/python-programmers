"""
N -> 크기,
w 가로, h 세로, k -> 택배번호
좌측 좌표 c
"""
def solution(N, box_list, box_find):
    box_maps = [[0]*N for _ in range(N)]
    box_dict = {}
    answer = []

    # 택배 쌓기
    # 층 단위로 계산했을 때 존재하면 바로 다음줄로 계산
    for k, h, w, c in box_list:
        is_build = False

        for y in range(N-1, -1, -1):
            can_build = True
            if is_build: break

            # 박스 채울 수 있는 지 체크
            for i in range(y, y-h, -1):
                if not can_build: break

                for j in range(c, c+w):
                    # 해당 위치에 블록이 있는 경우
                    if box_maps[i][j] != 0:
                        can_build = False
                        break

            # 박스 채우기
            if can_build:
                for a in range(y, y-h, -1):
                    for b in range(c, c + w):
                        box_maps[a][b] = k
                is_build = True
                box_dict[k] = (h, w, y, c)


    # 왼쪽 하차 -> 중력으로 떨어트림
    def left_out():
        # 택배 번호가 작은 것 빼기
        box_left_out = set()
        for check_num in box_find:
            is_find = True
            out_h, out_w, out_y, out_x = box_dict[check_num]
            for a in range(out_y, out_y - out_h, -1):
                if not is_find: break
                for b in range(out_x, -1, -1):
                    if box_maps[a][b] == check_num or box_maps[a][b] == 0:
                        continue
                    else:
                        is_find = False
            if is_find:
                box_left_out.add(check_num)

        box_left_out = list(box_left_out)
        box_left_out.sort()

        # 택배 번호 작은 것 빼기
        # 택배 존재 리스트, 정보 딕셔너리 삭제
        first_one = box_left_out.pop(0)
        # print("first_one", first_one)
        height, width, start_y, start_x = box_dict[first_one]
        box_find.remove(first_one)
        answer.append(first_one)

        # print("left_before")
        # print(box_maps)

        for i in range(start_y, start_y - height, -1):
            for j in range(start_x, start_x + width):
                box_maps[i][j] = 0
        del box_dict[first_one]

        # 중력 작용
        # 1. 영향을 받는 박스 단위로 처리해야한다
        # 2. 박스가 어디까지 내려갈 수 있는 지 계산
        # 3. 이때, 박스 전체가 다 들어올 수 잇는 지를 확인
        affect_box = []
        for box_num in box_find:
            h, w, y, x = box_dict[box_num]
            if y < start_y:
                affect_box.append(box_num)

        # y 순으로 정렬
        affect_box.sort(key=lambda t: -box_dict[t][2])

        # 어디까지 떨어짎 수 있는 지 계산
        for drop_num in affect_box:
            h, w, y, x = box_dict[drop_num]

            # 박스 넣기 전 그 공간 비우기
            for i in range(y, y-h, -1):
                for j in range(x, x+w):
                    box_maps[i][j] = 0

            # 사라진 블록 Y 위치서부터 쌓아보기
            drop = 0
            while True:
                new_bottom = y+1 + drop
                if new_bottom >= N:
                    break

                can_drop = True
                for r in range(new_bottom, new_bottom-h, -1):
                    if not can_drop: break
                    for c in range(x, x+w):
                        if box_maps[r][c] != 0:
                            can_drop = False
                            break

                if not can_drop:
                    break

                drop += 1

            # 박스 새로 넣기
            new_y = y + drop
            for i in range(new_y, new_y - h, -1):
                for j in range(x, x + w):
                    box_maps[i][j] = drop_num

            # 새 box_dict 반영
            box_dict[drop_num] = (h, w, new_y, x)

        # print("left_after")
        # print(box_maps)
        # print()

    # 오른쪽 빼기
    def right_out():
        # 택배 번호가 작은 것 빼기
        box_right_out = set()
        for check_num in box_find:
            is_find = True
            out_h, out_w, out_y, out_x = box_dict[check_num]
            for a in range(out_y, out_y-out_h, -1):
                if not is_find: break
                for b in range(out_x + out_w, N):
                    if box_maps[a][b] == check_num or box_maps[a][b] == 0:
                        continue
                    else:
                        is_find = False
            if is_find:
                box_right_out.add(check_num)

        box_right_out = list(box_right_out)
        box_right_out.sort()

        # 택배 번호 작은 것 빼기
        # 택배 존재 리스트, 정보 딕셔너리 삭제
        first_one = box_right_out.pop(0)
        # print("first_one", first_one)
        # print("right_before")
        # print(box_maps)
        height, width, start_y, start_x = box_dict[first_one]
        box_find.remove(first_one)
        answer.append(first_one)

        for i in range(start_y, start_y - height, -1):
            for j in range(start_x, start_x + width):
                box_maps[i][j] = 0
        del box_dict[first_one]

        # 중력 작용
        # 1. 영향을 받는 박스 단위로 처리해야한다
        # 2. 박스가 어디까지 내려갈 수 있는 지 계산
        # 3. 이때, 박스 전체가 다 들어올 수 잇는 지를 확인
        affect_box = []
        for box_num in box_find:
            h, w, y, x = box_dict[box_num]
            if y < start_y:
                affect_box.append(box_num)

        # y 순으로 정렬
        affect_box.sort(key=lambda t: -box_dict[t][2])

        # 어디까지 떨어짎 수 있는 지 계산
        for drop_num in affect_box:
            h, w, y, x = box_dict[drop_num]

            # 박스 넣기 전 그 공간 비우기
            for i in range(y, y - h, -1):
                for j in range(x, x + w):
                    box_maps[i][j] = 0

            # 사라진 블록 Y 위치서부터 쌓아보기
            drop = 0
            while True:
                new_bottom = y+1+drop
                if new_bottom >= N:
                    break

                can_drop = True
                for r in range(new_bottom, new_bottom - h, -1):
                    if not can_drop: break

                    for c in range(x, x + w):
                        if box_maps[r][c] != 0:
                            can_drop = False
                            break

                if not can_drop:
                    break

                drop += 1

            new_y = y + drop
            # 박스 새로 넣기
            for i in range(new_y, new_y - h, -1):
                for j in range(x, x + w):
                    box_maps[i][j] = drop_num

            # 새 box_dict 반영
            box_dict[drop_num] = (h, w, new_y, x)

        #print("right_after")
        #print(box_maps)
        #print()

    while box_find:
        left_out()
        right_out()

    for ans in answer:
        print(ans)


if __name__ == "__main__":
    N, M = map(int, input().split())
    box_list = []
    box_find = set()
    for _ in range(M):
        k, h, w, c = map(int, input().split())
        box_list.append((k, h, w, c-1))
        box_find.add(k)
    solution(N, box_list, box_find)