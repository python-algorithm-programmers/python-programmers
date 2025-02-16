from collections import deque
def solution(M,N,K,secret_cmd,total_cmd):
    # 비밀 식권보다 입력 커맨드가 적으면 무조건 normal
    if N < M:
        return 'normal'

    else:
        result = []
        queue = deque(secret_cmd)
        for cmd in total_cmd:
            first_one = queue.popleft()
            if first_one == cmd:
                result.append(first_one)
            else:
                # 큐, result 초기화
                queue = deque(secret_cmd)
                result = []

            # 종료 조건
            if result == secret_cmd:
                return 'secret'

    return 'normal'

if __name__ == "__main__":
    import sys
    M, N, K = list(map(int, sys.stdin.readline().strip().split(" ")))
    secret_cmd = list(map(int, sys.stdin.readline().strip().split(" ")))
    total_cmd = list(map(int, sys.stdin.readline().strip().split(" ")))
    print(solution(M,N,K,secret_cmd,total_cmd))