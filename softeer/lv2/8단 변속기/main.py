def solution(number_list):
    ascending = [i for i in range(1, 9)]
    descending = [i for i in range(8, 0, -1)]

    if len(number_list) == 8:
        if ascending == number_list:
            return 'ascending'
        elif descending == number_list:
            return 'descending'
        else:
            return 'mixed'

    if ascending in number_list:
        return 'ascending'
    elif descending in number_list:
        return 'descending'
    else:
        return 'mixed'

if __name__ == "__main__":
    import sys
    number_list = list(map(int, sys.stdin.readline().strip().split(" ")))
    print(solution(number_list))