import sys

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
sys.stdin = open('input.txt')
arr = input()[1:-1].split(", ")
print(arr)
max = 0
for i in arr:
    int_i = int(i)
    if max < int_i:
        max = int_i

print(max)