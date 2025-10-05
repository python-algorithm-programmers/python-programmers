from collections import defaultdict

def solution(gems):
    full_set = set(gems)
    start, end = 0, 0
    n = len(gems)
    answer = [start, n]

    full_cnt = len(full_set)
    jew_dict = {}
    jew_dict[gems[0]] = 1

    while start <= end and end < n:
        # 모든 보석이 포함됨, 그러면 이제부터는 start를 줄여봄
        print(start, end)
        if len(jew_dict) == full_cnt:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]

            jew_dict[gems[start]] -= 1
            if jew_dict[gems[start]] == 0:
                del jew_dict[gems[start]]
            start += 1
            continue

        if end == n - 1:
            break

        end += 1
        jew_dict[gems[end]] = jew_dict.get(gems[end], 0) + 1

    return [answer[0] + 1, answer[1] + 1]

if __name__ == "__main__":
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    print(solution(gems))
