user_dict = {}
def recording(command,user_id, user_name, result):
    if command == "Enter":
        # 기존에 입장 후, 새로 들어왔는 데, 이름이 바뀌어서 들어온 경우
        # 새로운 user_name으로 히스토리를 바꿔줘야함
        if user_id in user_dict and user_dict.get(user_id) != user_name:
            for i in range(len(result)):
                if user_id in result[i]:
                    result[i] = result[i].replace(f"{user_dict[user_id]}", user_name)

        # 새로 입장 한경우, 이름이 바뀌지 않은 채로 재입장한 경우
        user_dict[user_id] = user_name
        history = f"{user_dict[user_id]}={user_id}님이 들어왔습니다."
        result.append(history)

    elif command == "Leave":
        history = f"{user_dict[user_id]}={user_id}님이 나갔습니다."
        result.append(history)

    else:
        for i in range(len(result)):
            if user_id in result[i]:
                result[i] = result[i].replace(f"{user_dict[user_id]}", user_name)
                user_dict[user_id] = user_name

# ={dict_key} 삭제 로직
def wrap_up(result):
    for key in user_dict:
        for i in range(len(result)):
            result[i] = result[i].replace(f"={key}", "")

def solution(records):
    answer = []

    for record in records:
        record_list = record.split(" ")

        if len(record_list) == 3:
            command, user_id, user_name = record_list
            recording(command, user_id, user_name, answer)

        else:
            command, user_id = record_list
            recording(command, user_id, user_dict[user_id], answer)

    wrap_up(answer)
    return answer

if __name__ == '__main__':
    print(solution([
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
    "Leave uid4567",
    "Enter uid1234 Cat",
    "Enter uid3579 Dog",
    "Change uid3569 CuteDog",
    "Leave uid1234",
    "Leave uid3579"
    ]))