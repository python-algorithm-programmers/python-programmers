def solution(progresses, speeds):
    # 맨 앞 작업부터 작업완료까지 필요한 날짜 계산
    complete_list = []

    # 7일, 3일, 9일 -> list화
    for progress, speed in zip(progresses, speeds):
        date_count = (100 - progress - 1) // speed + 1
        complete_list.append(date_count)

    # 앞선 작업이 끝나지 않았으므로
    # 리스트에서 앞의 것보다 작은 것들은 일찍 끝나더라도 맨 앞 숫자때 같이 지워지는 로직
    answer = []

    while complete_list:
        count = 0
        first_deployment = complete_list[0]

        while complete_list and complete_list[0] <= first_deployment:
            complete_list.pop(0)
            count += 1

        answer.append(count)

    return answer

if __name__ == '__main__':
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))