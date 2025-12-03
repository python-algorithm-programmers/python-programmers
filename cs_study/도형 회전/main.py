from pprint import pprint
from collections import deque

# 90, -90 도형 회전
arrs = [[1,2,3], [4,5,6], [7,8,9]]
N = 3
# clockwise = [[0]*3 for _ in range(3)]
# counter_clockwise = [[0]*3 for _ in range(3)]
# for r in range(N):
#     for c in range(N):
#         counter_clockwise[r][c] = arrs[c][N-1-r]
#         clockwise[r][c] = arrs[N-1-c][r]
#
# pprint(arrs)
# pprint(clockwise)
# pprint(counter_clockwise)

# zip을 이용한 회전 = 직사각형도 된다
print()
print(list(map(list, zip(*[arr[::-1] for arr in arrs]))))
clock_zip = list(map(list, zip(*arrs[::-1])))
print(clock_zip)


# 리스트 회전
# clock_queue = deque(arrs)
# counter_queue = deque(arrs)
# clock_queue.rotate()
# counter_queue.rotate(-1)
# pprint(clock_queue)
# pprint(counter_queue)

# 테두리 회전
print()
N, M = 3, 4
new_arrs = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print(new_arrs)

"""
1. 테두리 추출 -> list로 따로 모음
2. 테두리 List -> deque로 해서 .rotate() or .rotate(-1)
3. 테두리 붙이기 (추출식으로)
    - top, bottom, left, right 정의
"""



# 테두리 추출
def extract(arrs):
    result = []
    # 시계 방향으로 추출
    # 맨윗줄
    for c in range(M-1):
        result.append(new_arrs[0][c])

    for r in range(N):
        result.append(new_arrs[r][M-1])

    for c in range(M-2, -1, -1):
        result.append(new_arrs[N-1][c])

    for r in range(1, N-1):
        result.append(new_arrs[r][0])
    return result

print(extract(new_arrs))

# 리스트 회전
def rotate(arrs: list, rotate_flag, k=1):
    queue = deque(arrs)
    if rotate_flag:
        queue.rotate(k)
    else:
        queue.rotate(-k)
    return list(queue)


# 테두리 채워넣기
def fill(arrs, vals):
    top, bottom = 0, N-1
    left, right = 0, M-1
    idx = 0

    # 위쪽
    for c in range(right):
        arrs[top][c] = vals[idx]
        idx += 1

    # 오른쪽
    for r in range(top, bottom):
        arrs[r][right] = vals[idx]
        idx += 1

    # 아래쪽
    for c in range(right, 0, -1):
        arrs[bottom][c] = vals[idx]
        idx += 1

    # 왼쪽
    for r in range(bottom, 0, -1):
        arrs[r][left] = vals[idx]
        idx += 1

vals = extract(new_arrs)
rotate_vals = rotate(vals, True, 1)
print(rotate_vals)
fill(new_arrs, rotate_vals)
print(new_arrs)