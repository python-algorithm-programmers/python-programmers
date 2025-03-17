from collections import deque
# 처음에 order에 위치한 값에 따라 바뀐다
# 두번째부터는 tmp나 belt에 있는 값에 유무에 따라 판단
# queue: order, belt
# stack: tmp

def solution(order):
    n = len(order)
    order_idx = 0
    belt_idx = 1
    tmp_stack = []

    while order_idx < n:
        # 그냥 belt에서 가져다 쓸 수 있는 경우
        if belt_idx == order[order_idx]:
            belt_idx += 1
            order_idx += 1

        # 보조 벨트에서 가져다 쓰는 경우
        elif tmp_stack and tmp_stack[-1] == order[order_idx]:
            tmp_stack.pop()
            order_idx += 1

        # 보조 벨트에 넣기
        elif belt_idx <= n:
            tmp_stack.append(belt_idx)
            belt_idx += 1

        # 아웃
        else:
            break

    return order_idx

if __name__ == "__main__":
    order = [4, 3, 1, 2, 5]
    print(solution(order))