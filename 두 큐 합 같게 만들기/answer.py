from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1 = sum(q1)
    sum2 = sum(q2)
    total = sum1 + sum2

    if total % 2 != 0:
        return -1  # 홀수는 나눌 수 없음

    target = total // 2
    count = 0
    max_count = len(queue1) * 3

    # 어짜피 한쪽의 queue에서 반쪽합만 만족하면 되면 그렇게 구현
    while count <= max_count:
        if sum1 == target:
            return count
        elif sum1 > target:
            num = q1.popleft()
            sum1 -= num
            q2.append(num)
        else:
            num = q2.popleft()
            sum1 += num
            q1.append(num)
        count += 1

    return -1

if __name__ == "__main__":
    queue1 = [3, 2, 7, 2]
    queue2 = [4, 6, 5, 1]
    print(solution(queue1, queue2))