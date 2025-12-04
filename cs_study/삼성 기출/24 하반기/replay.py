from pprint import pprint

def solution(R, C, golem_dict, K):
    forest_map = [[0]*C for _ in range(R+1)]
    answer = 0
    for idx in range(1, K+1):
        r_idx = -1
        end_flag = False
        print("idx", idx)
        while True:
            print("column", golem_dict[idx]["c"])
            golem_c = golem_dict[idx]["c"]
            golem_d = golem_dict[idx]["d"]

            # 남쪽에서 내려오기
            # -2번째 줄에서 -1번째 줄 들어올 수 있는 지 확인
            if r_idx == -1:
                if forest_map[0][golem_c] == 0:
                    r_idx += 1
                    continue
                else:
                    end_flag = True
                    break

            elif r_idx == 0:
                if forest_map[1][golem_c] == 0 \
                    and forest_map[0][golem_c-1] == 0\
                    and forest_map[0][golem_c+1] == 0:
                    r_idx += 1
                    continue

            else:
                if forest_map[r_idx+2][golem_c] == 0 \
                    and forest_map[r_idx+1][golem_c-1] == 0 \
                    and forest_map[r_idx+1][golem_c+1] == 0:
                    r_idx += 1

                    # 하단까지 온 경우라면
                    if r_idx == R-1:
                        end_flag = True
                        break
                    continue

            can_left = True
            if golem_c - 2 < 0:
                can_left = False

            if can_left:
                # 서쪽 이동, 가능하면 내려가고 다시 반복, 불가능하면 내려감
                if forest_map[r_idx-1][golem_c-1] == 0 \
                    and forest_map[r_idx][golem_c-2] == 0 \
                    and forest_map[r_idx+1][golem_c - 1] == 0\
                    and forest_map[r_idx+1][golem_c - 2] == 0\
                    and forest_map[r_idx + 2][golem_c - 1] == 0:
                    r_idx += 1

                    # 출구 반시계 이동
                    golem_dict[idx]["d"] = (golem_d - 1) % 4

                    # 서쪽 이동 반영
                    golem_dict[idx]["c"] = golem_c - 1

                    # 하단까지 온 경우라면
                    if r_idx == R - 1:
                        end_flag = True
                        break
                    continue

            # 동쪽 이동
            can_right = True
            if golem_c + 2 >= C:
                can_right = False

            if can_right:
                if forest_map[r_idx - 1][golem_c + 1] == 0 \
                        and forest_map[r_idx][golem_c + 2] == 0 \
                        and forest_map[r_idx + 1][golem_c + 1] == 0\
                        and forest_map[r_idx + 1][golem_c + 2] == 0\
                        and forest_map[r_idx + 2][golem_c + 1] == 0:
                    r_idx += 1

                    # 출구 시계 이동
                    golem_dict[idx]["d"] = (golem_d + 1) % 4

                    # 동쪽 이동 반영
                    golem_dict[idx]["c"] = golem_c + 1

                    # 하단까지 온 경우라면
                    if r_idx == R - 1:
                        end_flag = True
                        break
                    continue

            # 남쪽 -> 서쪽 -> 동쪽 이동 안되면 이건 중단임
            end_flag = True
            break

        # 반영
        if end_flag:
            if r_idx <= 1:
                forest_map = [[0] * C for _ in range(R + 1)]
                continue

            # 맵반영
            golem_c = golem_dict[idx]["c"]
            out_d = golem_dict[idx]["d"]
            forest_map[r_idx][golem_c] = idx
            for dy, dx in directions:
                ny, nx = r_idx+dy, golem_c+dx
                forest_map[ny][nx] = idx

            # 출구 위치 찾기
            out_dy, out_dx = directions[out_d]
            out_y, out_x = r_idx+out_dy, golem_c+out_dx
            print("out_where", out_y, out_x)

            # 출구 위치에서 4방 뒤져 보고 그 블록의 최댓값 반영
            max_result = 0
            for dy, dx in directions:
                my, mx = out_y+dy, out_x+dx
                if 0 <= my < R+1 and 0 <= mx < C and forest_map[my][mx] != 0 and forest_map[my][mx] != idx:
                    max_result = max(max_result, golem_dict[forest_map[my][mx]]["result"])


            pprint(forest_map)
            if max_result != 0:
                golem_dict[idx]["result"] = max_result
                answer += max_result
                print("max", max_result)
                continue

            # 주위에 어떠한 블록이 없는 경우
            golem_dict[idx]["result"] = r_idx+1
            answer += golem_dict[idx]["result"]
            print("solo", golem_dict[idx]["result"])
    return answer




if __name__ == "__main__":
    R, C, K = map(int, input().split())
    golem_dict = {}
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(1, K+1):
        start_x, out_dir = map(int, input().split())
        inner_struct = {}
        inner_struct["c"] = start_x - 1
        inner_struct["d"] = out_dir
        inner_struct["result"] = 0
        golem_dict[i] = inner_struct

    print(solution(R, C, golem_dict, K))