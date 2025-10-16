"""
분으로 바꿔서 풀기
- 9시 정각부터 n회 t분 간격, 최대 m명
- 정각에 도착한 사람도 타는 것
- timetable, 도착하는 친구들 시각

[목표]
콘이 셔틀을 버스 탈 수 있는 제일 늦은 시각
다만, 같은 시간에 도착한 크루중 대기열 제일 뒤에 섬

[과정]
제일 마지막 버스 시간이면서 늦은 시간에 올라타도 늦을 수 있는 지 물어본 것

[조건]
- 9시 정각부터 n회 t분 간격, 최대 m명
- 스택의 크기를 m만큼 지정하고 오는 버스대로(n개 나열) timetable값 넣기
0. 시간을 모두 minute으로 바꾸는 함수

1. 버스의 갯수 n개와 수용공간 m만큼 받을 수 있는 dictionary 생성
minute: [[], [], []]

2. time_table에 차례대로 dictionary에 넣기

"""

def change_to_minute(time_str):
    h, m = time_str.split(":")
    return int(h)*60 + int(m)

def minute_to_str(minute):
    h = minute // 60
    m = minute % 60
    h_str = str(h)
    m_str = str(m)
    if h < 10:
        h_str = f"0{h}"
    if m < 10:
        m_str = f"0{m}"
    return f"{h_str}:{m_str}"

def solution(n, t, m, timetable):
    time_dict = {540+t*i: [] for i in range(n)}
    time_keys = time_dict.keys()
    # 시간 넣기
    timetable.sort()
    queue_table = timetable[:]
    for dict_key in time_keys:
        while queue_table:
            if len(time_dict[dict_key]) < m:
                time = queue_table[0]
                minutes = change_to_minute(time)
                if minutes <= dict_key:
                    queue_table.pop(0)
                    time_dict[dict_key].append(minutes)
                else:
                    break

            else:
                break

    # 제일 시간이 나중인 key의 valuelist 크기가 m보다 작을 때 그 key값을
    # 값이 있는 데, [-1]인덱스의 값이 key값보다 작거나 같으면 -1해서 반환
    # key값보다 크면 key값을 반환
    #print(time_dict)
    last_bus_min, timelist = list(time_dict.items())[-1]
    if len(timelist) < m:
        return minute_to_str(last_bus_min)

    else:
        last_time = timelist[-1]
        if last_time <= last_bus_min:
            return minute_to_str(last_time-1)
        else:
            return minute_to_str(last_bus_min)


if __name__ == "__main__":
    n = 2
    t = 10
    m = 2
    timetable = ["09:10", "09:09", "08:00"]
    print(solution(n, t, m, timetable))