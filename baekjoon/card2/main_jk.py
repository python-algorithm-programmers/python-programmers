from collections import deque

def solution(N):
    n_list = [i for i in range(1, N+1)]
    queue = deque(n_list)

    while len(queue) > 1:
        # 맨 위가 맨 왼쪽으로 고려
        # 맨 처음 숫자 버리기
        queue.popleft()

        # 2번째 숫자 뒤로 넘기기
        second_num = queue.popleft()
        queue.append(second_num)

    return queue.pop()

if __name__ == "__main__":
    import sys
    lines = sys.stdin.readlines()
    N = int(lines[0].strip())
    print(solution(N))