from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    turn = 0
    sum1, sum2 = sum(q1), sum(q2)
    total = sum1 + sum2

    # 반쪽자리 합만 맞추면 되므로
    if total % 2 != 0:
        return -1
    target = total // 2

    # 이정도까지만 탐색
    safe_boundary = len(q1)*3

    while turn < safe_boundary:
        if sum1 == target:
            return turn

        elif sum1 > target:
            num = q1.popleft()
            q2.append(num)
            sum1 -= num

        else:
            num = q2.popleft()
            q1.append(num)
            sum1 += num

        turn += 1

    return -1


if __name__ == "__main__":
    queue1 = [3, 2, 7, 2]
    queue2 = [4, 6, 5, 1]
    print(solution(queue1, queue2))