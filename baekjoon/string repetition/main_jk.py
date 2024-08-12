import sys

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()
sentence = lines[0].strip()

# 공백이 있으면 그거로 split
words = sentence.split(" ")
print(len(words))