def bisect(stones, k, mid):
    zero_cnt = 0
    for stone in stones:
        if stone - mid <= 0:
            zero_cnt += 1
            if zero_cnt >= k:
                return False

        else:
            zero_cnt = 0
    return True

def solution(stones, k):
    # 이분 탐색은 건널 수 있는 사람 수라는 값의 범위에 대해 적용
    # 이분 탐색 대상은 사람 수, 경계 기준은 그 인원까지 건널 수 있는 지
    left, right = 1, max(stones)
    while left<=right:
        mid = (left + right) // 2
        if bisect(stones, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer + 1


if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones, k))