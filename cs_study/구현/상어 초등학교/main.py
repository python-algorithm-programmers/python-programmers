def solution(N, student_dict, maps):
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    for student_num, like_list in student_dict.items():
        like_match = []
        for y in range(N):
            for x in range(N):
                # 이미 차있는 칸은 배제
                if maps[y][x] != 0:
                    continue
                like_cnt = 0
                zero_cnt = 0
                for dy, dx in directions:
                    ny, nx = y+dy, x+dx
                    if 0<=ny<N and 0<=nx<N and maps[ny][nx] in like_list:
                        like_cnt += 1
                    if 0 <= ny < N and 0 <= nx < N and maps[ny][nx]==0:
                        zero_cnt += 1

                like_match.append((y,x,like_cnt,zero_cnt))
        # 좋아하는 사람 카운트 > 빈 공간 > 행의 값 > 열의 값 순으로 정렬
        like_match.sort(key=lambda x:(-x[2], -x[3], x[0], x[1]))
        # print(like_match)
        # print(student_num)
        # print()
        final_y, final_x, _, _ = like_match[0]
        maps[final_y][final_x] = student_num

    # 점수 매기기
    total_sum = 0
    for y in range(N):
        for x in range(N):
            sum_of_like_cnt = 0
            for dy, dx in directions:
                target_like_list = student_dict[maps[y][x]]
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and maps[ny][nx] in target_like_list:
                    sum_of_like_cnt += 1

            if sum_of_like_cnt > 0:
                total_sum += 10 ** (sum_of_like_cnt-1)
    return total_sum

if __name__ == "__main__":
    N = int(input().strip())
    raw_list = []
    maps = [[0]*N for _ in range(N)]
    student_dict = {}
    for _ in range(N*N):
        raw_list.append(list(map(int, input().strip().split())))
    for raw_line in raw_list:
        student_dict[raw_line[0]] = raw_line[1:]
    print(solution(N, student_dict, maps))