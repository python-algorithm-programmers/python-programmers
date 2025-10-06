def dfs(choice, result, cnt, n, answer):
    if cnt == n:
        result.add(tuple(sorted(choice[:])))
        return

    for show in answer[cnt]:
        if show not in choice:
            choice.append(show)
            dfs(choice, result, cnt + 1, n, answer)
            choice.pop()


def solution(user_id, banned_id):
    answer = []
    for ban_str in banned_id:
        split_answer = []
        for usr_str in user_id:
            if len(ban_str) != len(usr_str):
                continue
            else:
                answer_flag = True
                for ban_char, usr_char in zip(ban_str, usr_str):
                    if ban_char != '*' and ban_char != usr_char:
                        answer_flag = False
                        break

                if answer_flag:
                    split_answer.append(usr_str)

        answer.append(split_answer)

    # 조합 계산
    result = set()
    choice = []
    n = len(answer)
    dfs(choice, result, 0, n, answer)
    print(result)
    return len(result)

if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]
    print(solution(user_id, banned_id))