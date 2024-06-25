import sys

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()

originals = lines[0].strip()
answers = lines[1].strip()
check_answer = []

for original in originals:
    if original in '1234567890':
        check_answer.append(original)

check_answer_str = "".join(check_answer)
if answers in check_answer_str:
    print(1)

else:
    print(0)