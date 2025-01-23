def binary_search(order, menu_list):
    # 이진 탐색
    cur_min = 0
    cur_max = len(menu_list) - 1
    cur_guess = (cur_min + cur_max) // 2

    while cur_min <= cur_max:
        if menu_list[cur_guess] == order:
            return True

        elif menu_list[cur_guess] < order:
            cur_min = cur_guess + 1

        else:
            cur_max = cur_guess - 1

        # 다시 반영
        cur_guess = (cur_min + cur_max) // 2
    return False

def find_order(menu_list, order_list):
    menu_list.sort()
    order_list.sort()

    for order in order_list:
        if not binary_search(order, menu_list):
            return False
    return True


def find_menu(menu_list, order_list):
    return all(order in menu_list for order in order_list)


if __name__ == "__main__":
    import sys
    sys.stdin = open('input.txt')

    # 값 받기
    menu_list = input().split(", ")
    order_list = input().split(", ")
    # print(find_menu(menu_list, order_list))

    print(find_order(menu_list, order_list))



