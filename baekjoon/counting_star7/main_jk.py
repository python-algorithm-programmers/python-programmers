import sys

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()
n = int(lines[0].strip())

for i in range(2*n):
    if i <= n:
        print(' '*(n - i), end="")
        print('*'*(2 * i - 1))

    else:
        print(' ' * (i - n), end="")
        print('*'*(4 * n - 1 - 2 * i))