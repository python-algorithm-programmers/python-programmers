"""
건널 수 있다 <-> 건널 수 없다는 단조적인 조건 때문에 이분탐색이 가능
만약에 벽이나 랜덤한 장애물과 같은 조건이 생기면 이분 탐색 불가

"건널 수 있는 사람 수(x)”를 기준으로 할 때
x가 커질수록, ‘건널 수 있다’ → ‘건널 수 없다’로 단 한 번만 바뀌는 형태
x = 1 → 가능
x = 2 → 가능
x = 3 → 가능
x = 4 → 불가능
x = 5 → 불가능
"""
def can_cross(stones, k, mid):
    zero_cnt = 0
    for stone in stones:
        if stone - mid <= 0:  # mid명이 지나가면 0 이하인 돌
            zero_cnt += 1
            if zero_cnt >= k:  # 연속 k개면 못 건넘
                return False
        else:
            zero_cnt = 0
    return True  # 끝까지 통과했으면 가능


def solution(stones, k):
    left, right = 1, max(stones)
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if can_cross(stones, k, mid):  # mid명 건널 수 있나?
            answer = mid
            left = mid + 1   # 더 많은 인원 시도
        else:
            right = mid - 1  # mid명 불가능 → 줄임

    return answer+1


if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones, k))