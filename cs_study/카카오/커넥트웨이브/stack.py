"""
1 2 3 -> 1 stack Pop , 2, 3 stack pop
132, 321
이어지지 않으면, pop으로 간주

입력한 숫자를 저장할 stack을 줌
"""
def solution(arr):
    N = len(arr)
    next = 1 # 아직 스택에 넣지 않는 가장 작은 수
    stack = []
    # 목표 출력 수열을 순서대로 확인, 이번에 pop 되어야하는 값을 찾음
    for number in arr:
        # 이번에 넣어야할 값이 stack 맨 위에 오도록 하기 위해 push 반복
        # 쌓기, 빼야될 순간을 체크할 조건 넣기
        while next <= N and (not stack or stack[-1] != number):
            stack.append(next)
            next += 1
            print(stack)
            print(next)
            print()
        # 빼기
        if stack and stack[-1] == number:
            #print(stack[-1])
            stack.pop() # 출력을 의미
        else:
            return False
    return True

if __name__ == "__main__":
    print(solution([1, 4, 2, 3]))