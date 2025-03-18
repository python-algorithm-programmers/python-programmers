def solution(records):
    user_uid = {}
    answer_word = {
        "Enter": "님이 들어왔습니다.",
        "Leave": "님이 나갔습니다."
    }
    result = []
    for record in records:
        params = record.split(" ")
        if len(params) == 3:
            word, uid, name = params[0], params[1], params[2]

        else:
            word, uid = params[0], params[1]

        # Enter
        if word == "Enter":
            user_uid[uid] = name
            result.append((uid, word))

        # leave
        elif word == "Leave":
            result.append((uid, word))

        # change
        else:
            user_uid[uid] = name

    # 한꺼번에 끝내기
    return [user_uid[uid]+answer_word[word] for uid, word in result]

if __name__ == "__main__":
    records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(records))