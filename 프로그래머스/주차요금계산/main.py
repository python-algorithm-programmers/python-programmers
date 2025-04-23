from collections import deque
import math

def payment(park_time, default_time, base_fee, unit_time, percent):
    if park_time > default_time:
        # 올림 적용
        # *10을 한다음 //로 나눳을 때 1의 자리값이 있다면 +1
        extra_time = park_time-default_time
        return base_fee + math.ceil(extra_time / unit_time) * percent

    else:
        return base_fee

def solution(fees, records):
    default_time, default_fee, divider, percent = fees[0], fees[1], fees[2], fees[3]

    # hash로 받고 value는 (분 시간, 여부)로 튜플 리스트로 처리
    park_dict = {}
    result = []
    for record in records:
        hour_min, car_number, input_flag = record.split(" ")
        hour_min_list = list(map(int, hour_min.split(":")))
        total_minute = hour_min_list[0]*60 + hour_min_list[1]

        if not park_dict.get(car_number):
            park_dict[car_number] = []
        park_dict[car_number].append((total_minute, input_flag))

    # 리스트로 만들어서 minute 순으로 정렬
    sorted_park_list = sorted(park_dict.items(), key=lambda x:x[0])

    # 순서대로 요금 계산
    for car_number, time_flag_list in sorted_park_list:
        queue = deque(time_flag_list)
        total_park_time = 0
        while queue:
            minute_time, input_flag = queue.popleft()
            if input_flag == 'IN':
                if queue:
                    next_minute_time, next_input_flag = queue[0]
                    park_time = next_minute_time - minute_time
                    total_park_time += park_time
                    queue.popleft()
                else:
                    next_minute_time = 23*60 + 59
                    park_time = next_minute_time - minute_time
                    total_park_time += park_time

        final_fee = payment(total_park_time, default_time, default_fee, divider, percent)
        result.append(final_fee)

    return result


if __name__ == "__main__":
    fees = [120, 0, 60, 591]
    records = ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]
    print(solution(fees, records))