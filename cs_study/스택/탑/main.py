def solution(N, tower_list):
    answer = deque()

    # stack으로 앞에서부터 큰탑과 자기것만 남김
    # 인덱스는 유지할 수 잇도록 (index, height) 구조
    stack = []
    for i in range(N):
        cur = tower_list[i]

        # 신호를 못받는 좌측의 타워리스트 삭제
        while stack and stack[-1][1] < cur:
            stack.pop()

        if stack:
            answer.append(stack[-1][0])

        else:
            answer.append(0)

        # 자기꺼 등록
        stack.append((i+1, cur))

    return answer


if __name__ == "__main__":
    import sys
    from collections import deque

    input = sys.stdin.readline
    N = int(input())
    tower_list = list(map(int, input().split()))
    print(*solution(N, tower_list))