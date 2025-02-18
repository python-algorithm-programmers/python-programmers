def solution(total_list):
    result = []
    number_str_list = [str(i) for i in range(10)]

    for indirect, indexing in total_list:
        for i in range(len(indirect)):
            if indirect[i].upper() == 'X':
                # 숫자가 아닌 경우
                if indexing[i] not in number_str_list:
                    result.append(indexing[i].upper())

                # 숫자인 경우
                else:
                    result.append(indexing[i])

                # 찾았으니 다음으로 패스
                break

    return "".join(result)

if __name__ == "__main__":
    import sys
    N = sys.stdin.readline().strip()
    lines = sys.stdin.readlines()

    total_list = []
    for line in lines:
        str_list = line.strip().split(" ")
        total_list.append((str_list[0], str_list[1]))

    print(solution(total_list))
