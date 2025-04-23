def solution(sequence, k):
    n = len(sequence)
    left, right = 0, 0
    current_sum = sequence[0]
    best_range = [0, n - 1]  # 초기값 최대 길이

    while right < n:
        if current_sum == k:
            # 기존 best_range보다 길이가 짧거나, 같으면 더 앞쪽
            if (right - left) < (best_range[1] - best_range[0]):
                best_range = [left, right]

            current_sum -= sequence[left]
            left += 1

        elif current_sum < k:
            right += 1
            if right < n:
                current_sum += sequence[right]

        else:  # current_sum > k
            current_sum -= sequence[left]
            left += 1

    return best_range

if __name__ == "__main__":
    sequence = [1, 1, 1, 2, 3, 4, 5]
    k = 5
    print(solution(sequence, k))