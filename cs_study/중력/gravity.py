from pprint import pprint

boards = [
    ['X', 'X', 'X'],
    ['X', '.', '.'],
    ['.', 'X', '.'],
    ['.', '.', 'X']
]

"""
1. 행 기준, 열단위로 스캔하되 r값이 높은 아래쪽부터 블록을 스캔, 리스트 만듦
2. idx(N-1)를 설정, 블록 리스트를 아래에서부터 배치 + idx를 빼가기
    - 아예 그 열은 첨부터 다시 배치한다는 느낌으로
3. 줄어든 idx부터는 모두 빈공간으로 만들기
"""
N = len(boards)
M = len(boards[0])

def gravity(boards):
    for c in range(M):
        block_stack = []
        for r in range(N-1, -1, -1):
            if boards[r][c] == "X":
                block_stack.append(boards[r][c])

        # 쌓인 거만큼 블록 내리기
        idx = N-1
        for block in block_stack:
            boards[idx][c] = block
            idx -= 1

        # 나머지 idx만큼은 빈게 됨
        for r in range(idx, -1, -1):
            boards[r][c] = "."

gravity(boards)
print(boards)
