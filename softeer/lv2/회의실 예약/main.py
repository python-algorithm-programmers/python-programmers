# 조건
# 회의 시간 단위는 1시간
# 시작 - 종료 시간은 1시간 차
# 9~18까지 시각만 존재하고 출력할 때는 09로 표기해야함

# 풀이과정
# 방 이름 >> n available 수 >> 예약 가능한 시간대를 묶어서 표기
# 방 별로 key값을 분류하고, value는 리스트로 받자
# 9~18까지 리스트를 두고 하나씩 빼가는 과정

# 예시
# (10,11), (13,14), (16,17)
# 어떻게 시간 비는 지를 파악하는 게 중요
# 시간 간격간의 칸이 있다고 생각
# (9,18) -> (9,10) (11,18) ->(9,10) (11,13) (14,18) -> (9,10) (11,13) (14,16) (17,18)

def solution(room_list, reservation_dict):
    # 방 하나씩 탐색해가면서, 이때 없는 시간 대를 찾기
    # 방 별 빈 회의시간 저장 dict
    left_time_dict = {}
    room_list.sort()
    for idx, room in enumerate(room_list):
        left_time_dict[room] = [(9,18)]

        # 방별 빈시간을 뺀다? 옳은 방법은 아닌 것으로 사려됨
        for start_time, end_time in reservation_dict[room]:
            new_available = []

            for delta_start, delta_end in left_time_dict[room]:
                # 예약 시간이 기존 가용 시간과 완전히 일치하는 경우 (완전히 차지함)
                if delta_start == start_time and delta_end == end_time:
                    continue

                # 예약 시간이 시간대 내에 포함될 경우
                elif delta_start < start_time and end_time < delta_end:
                    new_available.append((delta_start, start_time))
                    new_available.append((end_time, delta_end))

                # 예약 시간이 기존 가용 시간의 왼쪽 일부만 차지하는 경우
                elif delta_start == start_time and end_time < delta_end:
                    new_available.append((end_time, delta_end))  # 오른쪽만 유지

                # 예약 시간이 기존 가용 시간의 오른쪽 일부만 차지하는 경우
                elif delta_start < start_time and delta_end == end_time:
                    new_available.append((delta_start, start_time))  # 왼쪽만 유지

                # 예약 시간이 기존 가용 시간과 겹치지 않는 경우 = 순전히 유지를 위해서 왜냐하면 뒤에서 업데이트 되니깐
                elif end_time <= delta_start or delta_end <= start_time:
                    new_available.append((delta_start, delta_end))

            # 업데이트해서 새로바뀐것만 적용해야됨
            left_time_dict[room] = new_available

        # 시간대 분류해서 미리 print 문 찍기
        print(f"Room {room}:")
        if left_time_dict[room]:
            print(f"{len(left_time_dict[room])} available:")
            for print_start, print_end in left_time_dict[room]:
                if print_start < 10:
                    print_start = f"0{print_start}"
                if print_end < 10:
                    print_end = f"0{print_end}"
                print(f"{print_start}-{print_end}")
        else:
            print("Not available")
        if idx < len(room_list) - 1:
            print("-----")

if __name__ == "__main__":
    import sys
    room_list = []

    N = sys.stdin.readline().strip()
    for i in range(3):
        room_list.append(sys.stdin.readline().strip())

    # 방 예약 건 확인
    reservation_dict = {}
    lines = sys.stdin.readlines()
    for line in lines:
        room_data = line.strip().split(" ")
        room, start, end = room_data[0], int(room_data[1]), int(room_data[2])
        if not reservation_dict.get(room):
            reservation_dict[room] = []
        reservation_dict[room].append((start, end))

    print(reservation_dict)
    solution(room_list, reservation_dict)


