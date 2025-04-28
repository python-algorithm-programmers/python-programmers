from collections import deque

def convert_minutes(time_str):
    hour, minute = map(int, time_str.split(":"))
    return hour*60 + minute

def solution(book_times):
    book_times = [(convert_minutes(start_time), convert_minutes(end_time)) for start_time, end_time in book_times]
    book_times.sort()
    queue = deque(book_times)
    room_dict = {}
    room_cnt = 0

    while queue:
        flag = True
        start_time, end_time = queue.popleft()

        # 룸을 for문 돌아서 여분 예약 가능 공간 확인
        # 전 시간에 대해서도 고민해봐야됨
        for i in range(len(room_dict)):
            # 동일한 룸에 있는 지도 확인
            for j in range(len(room_dict[i])):
                # 퇴실 후 10분 이상 여유가 있을 때 가능
                if room_dict[i][j][1] + 10 > start_time:
                    break

            else:
                # for문 다 돌았는데 break 안걸렸다 → 이 방은 가능
                room_dict[i].append((start_time, end_time))
                flag = False
                break


        # 만약 모든 룸에서도 추가가 안되는 상황이라면, 새로운 룸 등록
        if flag and not room_dict.get(room_cnt):
            room_dict[room_cnt] = []
            room_dict[room_cnt].append((start_time, end_time))
            room_cnt += 1

    print(room_dict)
    return room_cnt

if __name__ == "__main__":
    book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
    print(solution(book_time))