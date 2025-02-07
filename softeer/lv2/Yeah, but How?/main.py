# 큐로 풀자
from collections import deque
def solution(T):
    list_t = list(T)
    queue = deque(list_t)
    result = []
    while queue:
        cur_q = queue.popleft()

        # 종료조건
        if len(queue) == 0:
            result.append(cur_q)
            break

        if cur_q == '(':
            if queue[0] == '(':
                result.append(cur_q)
            else:
                result.append(cur_q)
                # 괄호가 닫힌 것이므로 1도 추가
                result.append('1')

        else:
            if queue[0] == '(':
                result.append(cur_q)
                result.append('+')
            else:
                result.append(cur_q)

    return "".join(result)



if __name__ == "__main__":
    import sys
    T = sys.stdin.readline().strip()
    print(solution(T))
