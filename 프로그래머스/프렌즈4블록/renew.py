from collections import deque


def solution(m,n,board):
    # 문자열을 분해해서 각각 문자가 담긴 리스트 형태로 바꾸기
    board = [list(row) for row in board]
    result = 0

    while True:
        # 지워야할 인덱스가 중복되지 않도록
        # 두번지우면 연이서 지워지니깐
        to_remove = set()

        # 최대 -1 크기를 갖도록 해서 다음 인덱스도 유추 가능하도록
        # 빼야될 인덱스 항목들 찾기
        for y in range(m-1):
            for x in range(n-1):
                check_point = board[y][x]
                if check_point == '0':
                    continue
                if check_point == board[y+1][x] and check_point == board[y][x+1] and check_point == board[y+1][x+1]:
                    to_remove.update([(y,x), (y+1,x), (y,x+1), (y+1,x+1)])


        # 빼야할 목록들 마킹
        if not to_remove:
            break

        # 0 표시
        for y,x in to_remove:
            board[y][x] = '0'
        result += len(to_remove)

        # 0 표시 된것들 제외해서 블록 떨구기
        # x부터 고정해서 y축 기준으로 블록 떨구기
        for x in range(n):
            queue = deque()
            for y in range(m-1, -1, -1):
                if board[y][x] != '0':
                    queue.append(board[y][x])
            for y in range(m-1, -1, -1):
                board[y][x] = queue.popleft() if queue else '0'

    return result

if __name__ == "__main__":
    m,n = 4,5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    print(solution(m,n,board))