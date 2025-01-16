# 연속으로 인덱스 설정 가능한 경우
# 숫자 뒤집기로 같은 숫자만 되는 것으로 최소 횟수
# = 연속되지 않은 숫자의 경우의 수

from collections import deque
def solution(num_str):
    # 한개인 경우
    if len(num_str) == 1:
        return 1

    queue = deque(num_str)
    cnt = 0
    flag = True

    while len(queue) > 1:
        # 처음 빼낸 것
        char = queue.popleft()

        # 다음꺼와 비교
        if char != queue[0]:
            if flag:
                cnt += 1
            flag = not flag

    return cnt


if __name__ == "__main__":
    # import sys
    # sys.stdin = open('input.txt')
    num_str = input().strip()  # 문자열의 앞뒤 공백 제거
    print(solution(num_str))
