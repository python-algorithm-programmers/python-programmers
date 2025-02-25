from functools import reduce
def solution(cloth_list):
    cloth_dict = {}
    for cloth in cloth_list:
        if not cloth_dict.get(cloth[1]):
            cloth_dict[cloth[1]] = []
        cloth_dict[cloth[1]].append(cloth[0])

    result = [len(v)+1 for k, v in cloth_dict.items()]

    # 1개씩
    return reduce(lambda x, y: x*y, result)-1


if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))