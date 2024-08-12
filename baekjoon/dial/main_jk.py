import sys


# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()
dial = lines[0].strip()

# 대문자 리스트
aList = [chr(i).upper() for i in range(ord('a'), ord('z')+1)]

# dial dictionary
dial_dict = {}
for i in range(2, 10):
    dial_dict[i] = []
    for alpha in aList:
        dial_dict[i].append(alpha)
        if len(dial_dict[i]) == 3:
            if i == 7 or i == 9:
                dial_dict[i].append(aList[3])
                aList = aList[4:]
                break
            else:
                aList = aList[3:]
                break


# 다이얼 시간 출력
# value로 key 값 찾기
answer = 0
for chr in dial:
    for k, v_list in dial_dict.items():
        if chr in v_list:
            answer += k+1

print(answer)
