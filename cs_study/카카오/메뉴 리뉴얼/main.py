def dfs(idx, choice, n, result, order, course):
    if idx == n:
        if len(choice) >= 2:
            result.add(choice)
        return

    dfs(idx + 1, choice, n, result, order, course)
    choice += order[idx]
    dfs(idx + 1, choice, n, result, order, course)
    choice = choice[:-1]


def solution(orders, course):
    answer = []
    menu_dict = {}
    for order in orders:
        choice = ""
        result = set()
        n = len(order)
        sorted_order = "".join(sorted(list(order)))
        dfs(0, choice, n, result, sorted_order, course)
        for menu_pick in result:
            menu_dict[menu_pick] = menu_dict.get(menu_pick, 0) + 1

    best_len = {}
    # 최빈값 구하고
    for name, count in menu_dict.items():
        if count < 2:
            continue

        length = len(name)
        if length in course:
            best_len[length] = max(best_len.get(length, 0), count)

    # 구한 최빈값을 answer에 넣기
    for name, count in menu_dict.items():
        if len(name) in best_len and count == best_len[len(name)]:
            answer.append(name)

    answer.sort()
    return answer

if __name__ == "__main__":
    orders = ["XYZ", "XWY", "WXA"]
    course = [2,3,4]
    print(solution(orders, course))