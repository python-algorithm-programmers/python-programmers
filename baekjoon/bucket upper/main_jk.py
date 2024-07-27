import sys

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()

# 숫자 리스트, 순서 바꾸는 로직 초기화
input_list = []
n, m = 0, 0
n, m = map(int, lines[0].strip().split())

for line in lines[1:m+1]:
    input_list.append(list(map(int, line.strip().split())))

result = [i for i in range(1, n+1, 1)]
for input in input_list:
    start = input[0] - 1
    end = input[1] - 1
    result = result[:start] + result[start:end+1][::-1] + result[end+1:]

result = ' '.join(map(str,result))
print(result)