def is_big(mid, times, n):
    check = 0
    for time in times:
        check += mid // time

    if check >= n:
        return True
    else:
        return False


def solution(n, times):
    left, right = 0, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        if is_big(mid, times, n):
            right = mid - 1

        else:
            left = mid + 1

    return left