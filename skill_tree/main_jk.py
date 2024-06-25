def solution(skill, skill_trees):
    cnt = 0

    # skill의 글자들 외에 다른 글자들 모두 삭제
    # 그러면 skill과 관련된 알파벳만 남는 데,
    skill_list = list(skill)
    for skill_tree in skill_trees:
        filtered_tree = "".join([skill_char for skill_char in skill_tree if skill_char in skill_list])

        # skill에 없는 다른 알파벳만 존재하면, skill 순서에 관계없이 가능한 스킬트리가 됨
        if len(filtered_tree) == 0:
            cnt += 1

        # 맨처음 스킬이 선행되어야 모든 스킬트리가 유효함
        elif filtered_tree[0] == skill[0]:

            # 순서를 올바르게 지킨 경우엔 맨처음 글자가 존재하는 조건에서의 "in" 조건은 허용되는 스킬트리에 해당
            if filtered_tree in skill:
                cnt += 1

            # 순서가 스킬과 다른, 즉 순서가 바뀌어 허용되지 않는 스킬트리는 in의 조건문에 포함되지 않음
            else:
                continue

    return cnt

if __name__ == '__main__':
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "CAD"]))