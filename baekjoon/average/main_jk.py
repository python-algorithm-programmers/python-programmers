import sys
from functools import reduce

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()

n = int(lines[0].strip())
num_list = list(map(int, lines[1].strip().split()))
max_value = max(num_list)

# 평균 구하기
# reduce(function, iterable, initializer)
# function: 두 개의 인자를 받는 함수. 첫 번째 인자는 누적기(acc), 두 번째 인자는 현재의 요소(x)
result = reduce(lambda acc, x: acc + (x/max_value), num_list, 0) * 100
result = result / len(num_list)
print(result)
