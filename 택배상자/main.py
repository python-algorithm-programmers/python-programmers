from collections import deque
# 처음에 order에 위치한 값에 따라 바뀐다
# 두번째부터는 tmp나 belt에 있는 값에 유무에 따라 판단
# queue: order, belt
# stack: tmp

def solution(order):
    # step 1: tmp 위치시키기
    belt = [i+1 for i in range(len(order))]
    belt_q = deque(belt)
    order_q = deque(order)
    tmp_stack = []
    result = []

    # tmp 위치시키지 않고도 작업이 가능한 경우
    while order_q:
        # 첫 숫자 전까지 tmp_stack에 저장
        first_order = order_q.popleft()

        # belt에서 first_one 위치확인
        first_order_idx = belt_q.index(first_order)

        # 보조 벨트를 안써도 되는 경우
        if first_order_idx == 0:
            first_belt_one = belt_q.popleft()
            result.append(first_belt_one)

        # 보조 벨트를 써야되는 경우
        else:
            for j in range(first_order_idx):
                belt_thing = belt_q.popleft()
                tmp_stack.append(belt_thing)

            # 보조 벨트에서 가져올 지 확인
            if tmp_stack[-1] == first_order:
                last_tmp_one = tmp_stack.pop()
                result.append(last_tmp_one)

            # 직접 벨트에서 가져옴
            elif belt_q[0] == first_order:
                first_belt_thing = belt_q.popleft()
                result.append(first_belt_thing)

            # 가져올 수 없는 경우
            else:
                break

    return result

if __name__ == "__main__":
    order = [4, 3, 1, 2, 5]
    print(solution(order))