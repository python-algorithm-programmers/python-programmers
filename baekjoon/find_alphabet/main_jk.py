import sys
import string

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()
word = lines[0].strip()

# 알파벳 리스트
alphabet_list = [alphabet for alphabet in string.ascii_lowercase]

# 인덱스 위치 출력
result = []
for alphabet in alphabet_list:
    if alphabet in word:
        result.append(word.index(alphabet))
    else:
        result.append(-1)

print(' '.join(list(map(str, result))))