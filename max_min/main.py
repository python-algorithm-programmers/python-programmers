def solution(A,B):
    sort_a = sorted(A)
    sort_b = sorted(B, reverse=True)

    answer = 0
    for a, b in zip(sort_a, sort_b):
        answer += a*b

    return answer

if __name__ == '__main__':
    print(solution([1, 4, 2], [5, 4, 3]))