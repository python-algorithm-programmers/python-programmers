import sys

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()

num_count = lines[0].strip()
num_list = list(map(int, lines[1].strip().split(" ")))
num_list.sort()

# 에라토스테네스의 체 이용
# 소수의 경우는 약수가 2개뿐이니깐, 각 배열의 값이 2인 것들만 찾으면 되거든
def get_divisor(num_list):
    max_num = max(num_list)
    divisor = [0] * (max_num+1)
    for i in range(1, max_num+1):
            for j in range(i, max_num+1, i):
                divisor[j] += 1

    return divisor

cnt = 0
divisor_list = get_divisor(num_list)
for i in range(1, len(divisor_list)):
    if (divisor_list[i] == 2) and i in num_list:
        cnt += 1

print(cnt)
