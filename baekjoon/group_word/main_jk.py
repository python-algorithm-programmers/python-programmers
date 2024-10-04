import sys

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()
num_count = int(lines[0].strip())

cnt = 0
for i in range(1, num_count+1):
    stack = []
    flag = True
    for char in lines[i].strip():
        if not stack:
            stack.append(char)

        # 이전 마지막 글자는 아니면서,
        elif stack[-1] != char:
            # 이전 포함 리스트에는 있는 경우
            if char in stack:
                flag = False
                break

            # 이전 포함 리스트에 없는 경우는 새 원솔로 추가
            else:
                stack.append(char)

    if flag:
        cnt += 1

print(cnt)