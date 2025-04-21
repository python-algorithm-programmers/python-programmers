def solution(sequence, k):
    n = len(sequence)
    left, right = 0, 0
    final_sum = sequence[0]
    best_seq = [0, n-1]

    while right < n:
        # 최초 한번에 등록해서, 인덱스가 작은 것은 고려할 필요가 없게 됨
        if final_sum == k:
            if right - left < best_seq[1] - best_seq[0]:
                best_seq = [left, right]

            final_sum -= sequence[left]
            left += 1

        elif final_sum < k:
            # right을 밖으로 빼서 while문 종료되도록
            right += 1
            if right < n:
                final_sum += sequence[right]

        else:
            final_sum -= sequence[left]
            left += 1

    return best_seq


if __name__ == "__main__":
    sequence = [1, 1, 1, 2, 3, 4, 5]
    k = 5
    print(solution(sequence, k))