import sys

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()
hour, minute = lines[0].strip().split(' ')
hour, minute = int(hour), int(minute)

# 시간 빼기
minute -= 45
if minute < 0:
    minute += 60
    hour -= 1
    if hour < 0:
        hour += 24

    print(f"{hour} {minute}")
else:
    print(f"{hour} {minute}")
