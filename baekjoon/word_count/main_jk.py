import sys

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()
test_cnt = int(lines[0].strip())

# 테스트 기록을 위한 딕셔너리 생성
test_dict = {}
for line in lines[1:]:
    repetition_cnt, input_str = line.strip().split(" ")
    test_dict[input_str] = int(repetition_cnt)

# 각 테스트별로 문자열 반복 실행
result = []
for input_str, repetition_cnt in test_dict.items():
    repeated_str = ''
    for char in input_str:
        repeated_str += char * repetition_cnt
    result.append(repeated_str)

# 결과 출력
for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i], end='')
    else:
        print(result[i])