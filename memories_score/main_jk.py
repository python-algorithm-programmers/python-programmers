def solution(names, yearnings, photos):
    name_dict = {}
    for name, yearning in zip(names, yearnings):
        name_dict[name] = yearning

    answer = []
    for photo in photos:
        score = 0
        for member in photo:
            if name_dict.get(member):
                score += name_dict[member]

        answer.append(score)
    return answer


if __name__ == '__main__':
    print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))