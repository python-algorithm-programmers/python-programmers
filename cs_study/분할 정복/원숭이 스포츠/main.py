"""
[조건]
원숭이를 2개 그룹으로 나눠서 진행, 각 팀에는 최소 한마리 원숭이
모든 두 원숭이에 대해서 적어도 한번은 적으로 만나도록 대진
7일간 진행하므로 7줄로 구성해야함

[판단]
Day1에 2개의 팀을 나누면, day2부터는 4개의 그룹, day3부터는 8개의 그룹으로 늘어남
리프 그룹은 2^7개의 그룹을 가짐 = 트리의 높이가 7인 이진트리

[예시]
["A", "B", "A", "B", "A", "B"]
["B", "A", "B", "A", "A", "B"]

[구성]
1. 분할
- 0번부터 6번 인덱스의 전체 원숭이 팀을 절반 나누기

2. 정복
- 같은 팀이었던 것들에 대해 팀을 2개의 그룹으로 나눈 것으로 재귀 처리

3. 결합
- 하위 분할에서 했던 것을 합쳐서 return
"""
def bisect_conquer(N, monkey_list, day, all_day, reverse_flag=False):
    # 마지막 리프 그룹에 도달했을 때
    if day == 7 or len(monkey_list) == 1:
        return

    # 원숭이 2개의 그룹 나누기, 대강 절반으로 분할
    mid = len(monkey_list) // 2
    a_group = monkey_list[:mid]
    b_group = monkey_list[mid:]

    for a in a_group:
        all_day[day][a] = "A" if not reverse_flag else "B"
    for b in b_group:
        all_day[day][b] = "B" if not reverse_flag else "A"

    # conquer
    bisect_conquer(N, a_group, day+1, all_day, reverse_flag)
    bisect_conquer(N, b_group, day + 1, all_day, not reverse_flag)

def solution(N):
    monkey_list = [i for i in range(N)]
    # 모든 날의 팀 배정을 저장할 변수
    all_day = [["A"] * N for _ in range(7)]
    bisect_conquer(N, monkey_list, 0, all_day)
    return ["".join(today) for today in all_day]



if __name__ == "__main__":
    N = int(input())
    for line_data in solution(N):
        print(line_data)
