def solution(n, queue):
    result_queue = deque()
    while queue:
        transmit_device = queue.popleft()
        return_flag = True
        for item in queue:
            if transmit_device[0] < item[0]:
                result_queue.appendleft(item[1])
                return_flag = False
                break

        # 없는 경우
        if return_flag:
            result_queue.appendleft(0)

    return list(result_queue)


if __name__ == "__main__":
    import sys
    from collections import deque
    n = list(map(int, sys.stdin.readline().strip()))
    queue = deque()
    for idx, height in enumerate(map(int, sys.stdin.readline().strip().split(" "))):
        queue.appendleft((height, idx+1))

    print(solution(n, queue))
