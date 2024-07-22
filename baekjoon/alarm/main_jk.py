import sys

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()
hour, minute = lines[0].strip().split(' ')

# 양쪽 끝의 공백을 제거 = strip()
num_list = [int(num.strip()) for num in lines]
remainder_list = []
for num in num_list:
    remainder = num % 42
    if remainder not in remainder_list:
        remainder_list.append(remainder)

print(len(remainder_list))