import sys

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()

num_cnt = int(lines[0].strip())
num_str = lines[1].strip()

print(sum([int(str) for str in num_str]))