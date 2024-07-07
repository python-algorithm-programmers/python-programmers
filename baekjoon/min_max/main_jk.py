import sys

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()

num_count = lines[0].strip()
num_list = lines[1].strip().split()
min = float("inf")
max = float("-inf")

for num in num_list:
    num = float(num)
    if min > num:
        min = num
    if max < num:
        max = num

print(f"{int(min)} {int(max)}")