def solution(big_list):
    rank_list = [1] * len(big_list)
    for i in range(len(big_list)):
        for j in range(len(big_list)):
            if i != j:
                if big_list[i][0] < big_list[j][0] and big_list[i][1] < big_list[j][1]:
                    rank_list[i] += 1

    return rank_list


if __name__ == '__main__':
    import sys
    lines = sys.stdin.readlines()
    big_list = []
    for line in lines[1:]:
        W, H = line.strip().split()
        big_list.append((int(W), int(H)))

    print(' '.join(map(str, solution(big_list))))