import sys

# 모든 입력을 줄 단위로 읽어서 리스트로 저장
lines = sys.stdin.readlines()
two_data = lines[0].strip()

# 공백이 있으면 그거로 split
word1, word2 = (two_data.split(" "))

# 뒤집고 int화
word1 = int(word1[::-1])
word2 = int(word2[::-1])

print(word1 if word1 > word2 else word2)