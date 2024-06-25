def solution(records):
    user_dict = {}
    result = []

    # 레코드 파싱 및 처리
    for record in records:
        tokens = record.split()
        command = tokens[0]
        user_id = tokens[1]

        if command == "Enter":
            user_name = tokens[2]
            user_dict[user_id] = user_name
            result.append((user_id, "님이 들어왔습니다."))

        elif command == "Leave":
            result.append((user_id, "님이 나갔습니다."))

        elif command == "Change":
            user_name = tokens[2]
            user_dict[user_id] = user_name

    # 최종 결과 생성
    answer = []
    for user_id, message in result:
        answer.append(f"{user_dict[user_id]}{message}")

    return answer


# 테스트
print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
