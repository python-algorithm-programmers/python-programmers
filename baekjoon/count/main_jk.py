import sys

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()

total_cnt = int(lines[0].strip())
num_list = lines[1].strip().split()
find_num = lines[2].strip()

cnt = 0
for num in num_list:
    if find_num == num:
        cnt += 1

print(cnt)
