import sys
import string

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()
n = int(lines[0].strip())

# 피보나치 구현 배열
num_arr = [0] * 1000000
num_arr[1] = 1

# 피보나치 배열 값 결정
for i in range(2, n+1):
    num_arr[i] = num_arr[i-1] + num_arr[i-2]

print(num_arr[n])