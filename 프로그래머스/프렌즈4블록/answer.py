def solution(m, n, board):
    # 문자열 리스트를 리스트의 리스트로 변환
    board = [list(row) for row in board]
    result = 0

    while True:
        # 지울 불록 인덱스 담는 세트
        # 세트로 담는 이유는 인덱스가 중복될 수 있으니깐
        to_remove = set()

        # 2x2 블록 탐색
        for y in range(m - 1):
            for x in range(n - 1):
                block = board[y][x]
                if block == '0':
                    continue
                if block == board[y][x + 1] and block == board[y + 1][x] and block == board[y + 1][x + 1]:
                    to_remove.update([(y, x), (y, x + 1), (y + 1, x), (y + 1, x + 1)])

        # 더 이상 지울 것이 없다면 종료
        if not to_remove:
            break

        # 블록 지우기
        for y, x in to_remove:
            board[y][x] = '0'
        result += len(to_remove)

        # 블록 떨어뜨리고, 다시 생성
        for x in range(n):
            stack = []
            for y in range(m - 1, -1, -1):
                if board[y][x] != '0':
                    stack.append(board[y][x])
            for y in range(m - 1, -1, -1):
                board[y][x] = stack.pop(0) if stack else '0'

    return result

if __name__ == "__main__":
    m,n = 4,5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    print(solution(m, n, board))