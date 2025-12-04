from pprint import pprint

def solution(R, C, golem_dict, K):
    forest_map = [[0]*C for _ in range(R+1)]
    answer = 0
    print(golem_dict)
    for idx in range(1, K+1):
        r_idx = 0
        end_flag = False
        moved_side = False
        print("idx", idx)
        while True:
            golem_c = golem_dict[idx]['c']
            golem_dy, golem_dx = golem_dict[idx]['d']
            if r_idx + 2 >= R + 2:
                end_flag = True
                break

            # 초반부 검증 -> 안 되면 map 갈고, 다음 것으로
            if r_idx == 0:
                if forest_map[r_idx+2][golem_c] == 0:
                    r_idx += 1
                    continue
                else:
                    end_flag = True
                    break

            elif r_idx == 1:
                if forest_map[r_idx + 2][golem_c] == 0 \
                    and forest_map[r_idx + 1][golem_c - 1] == 0 \
                    and forest_map[r_idx + 1][golem_c + 1] == 0:
                    r_idx += 1
                    continue
                else:
                    end_flag = True
                    break

            else:
                # 남쪽 검증, 이 조건을 통과하면 내려간다는 의미
                print("south_start", r_idx)
                pprint(forest_map)
                if forest_map[r_idx+2][golem_c] == 0 \
                    and forest_map[r_idx+1][golem_c - 1] == 0 \
                    and forest_map[r_idx+1][golem_c + 1] == 0:
                    r_idx += 1
                    moved_side = False
                    print("south complete")

                    if r_idx == R:
                        print("all down")
                        end_flag = True
                        break
                    continue

            if moved_side:
                end_flag = True
                break

            # 서쪽 검증
            # 바깥 영역인 지 확인, 바깥쪽이면 다음 step
            boundary_left = False
            if golem_c-2 < 0:
                boundary_left = True

            # 바깥 영역이 아니면 내부 값 검증
            print("left_start", r_idx)
            pprint(forest_map)
            if not boundary_left:
                if forest_map[r_idx][golem_c-2] == 0 \
                    and forest_map[r_idx-1][golem_c - 1] == 0 \
                    and forest_map[r_idx+1][golem_c - 1] == 0:
                    golem_c -= 1
                    golem_dict[idx]['c'] = golem_c

                    # 시계 방향으로 출구 회전
                    golem_dict[idx]['d'] = [golem_dx, -golem_dy]
                    print("left complete")
                    moved_side = True
                    continue

            # 동쪽 검증
            # 바깥 영역
            boundary_right = False
            if golem_c+2 >= C:
                boundary_right = True

            print("right_start", r_idx)
            pprint(forest_map)
            if not boundary_right:
                if forest_map[r_idx][golem_c + 2] == 0 \
                    and forest_map[r_idx - 1][golem_c + 1] == 0 \
                    and forest_map[r_idx + 1][golem_c + 1] == 0:
                    golem_c += 1
                    golem_dict[idx]['c'] = golem_c

                    # 반시계 방향으로 출구 회전
                    golem_dict[idx]['d'] = [-golem_dx, golem_dy]
                    print("right complete")
                    moved_side = True
                    continue

            # 3방향 검증했는 데 안되면 결과 반영
            end_flag = True
            break

        # 결과 반영
        if end_flag:
            print("result_start", r_idx)
            pprint(forest_map)

            if r_idx <= 2:
                forest_map = [[0] * C for _ in range(R)]
                continue

            # 맵 반영
            golem_c = golem_dict[idx]['c']
            forest_map[r_idx][golem_c] = idx
            # 4방향 모두 반영
            for dy, dx in directions:
                my, mx = r_idx+dy, golem_c+dx
                forest_map[my][mx] = idx

            # 출구 지점 계산
            golem_dy, golem_dx = golem_dict[idx]['d']
            out_y, out_x = r_idx + golem_dy, golem_c + golem_dx

            # 출구 지점에서 다른 것이 있는 지 탐색
            max_result = 0
            for dy, dx in directions:
                ny, nx = out_y+dy, out_x+dx
                if 0 <= ny < R and 0 < nx < C and forest_map[ny][nx] != 0 \
                    and forest_map[ny][nx] != idx:
                    max_result = max(max_result, golem_dict[forest_map[ny][nx]]['result'])
            if max_result != 0:
                golem_dict[idx]['result'] = max_result
                answer += max_result
                continue

            # 만약에 다른 것들이 없으면
            golem_dict[idx]['result'] = r_idx + 2
            answer += golem_dict[idx]['result']
            print(f"{idx} result out")
            pprint(forest_map)

    return answer

if __name__ == "__main__":
    R, C, K = map(int, input().split())
    golem_dict = {}
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(1, K+1):
        start_x, out_dir = map(int, input().split())
        inner_struct = {}
        inner_struct["c"] = start_x - 1
        inner_struct["core"] = []

        dir_dy, dir_dx = directions[out_dir]
        inner_struct["d"] = [dir_dy, dir_dx]
        inner_struct["result"] = 0
        golem_dict[i] = inner_struct

    print(solution(R, C, golem_dict, K))