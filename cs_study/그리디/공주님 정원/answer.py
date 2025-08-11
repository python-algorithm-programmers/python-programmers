def day_maker(m, d):
    return m*100 + d

def solution(N, flower_maps):
    cur_date = START

    # while문 기준 날짜
    idx = 0
    answer = 0

    while cur_date < END:
        best_end_date = cur_date
        while idx < len(flower_maps) and day_maker(flower_maps[idx][0], flower_maps[idx][1]) <= cur_date:
            best_end_date = max(day_maker(flower_maps[idx][2], flower_maps[idx][3]), best_end_date)
            idx += 1

        if best_end_date == cur_date:
            return 0

        answer += 1
        cur_date = best_end_date

    return answer


if __name__ == "__main__":
    import sys
    flower_maps = []
    N = int(sys.stdin.readline().strip())
    for _ in range(N):
        line = list(map(int, sys.stdin.readline().strip().split()))
        start_month, start_day, end_month, end_day = line[0], line[1], line[2], line[3]
        # 솎아내기
        if 3<=end_month and start_month<=11:
            flower_maps.append((start_month, start_day, end_month, end_day))

    # END는 그 날짜는 빼므로 12월 1일가지 필요
    START, END = 301, 1201

    # 정렬
    flower_maps.sort(key=lambda x: (x[0], x[1], -(x[2] * 100 + x[3])))
    print(solution(N, flower_maps))