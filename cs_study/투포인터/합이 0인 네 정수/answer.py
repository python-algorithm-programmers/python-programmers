def solution(N, A, B, C, D):
    # B-C, A-D 합치기
    BC = {}
    answer = 0

    for b in B:
        for c in C:
            BC[b+c] = BC.get(b+c, 0) + 1

    for a in A:
        for d in D:
            answer += BC.get(-(a+d), 0)

    return answer

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N = int(input())
    A, B, C, D = [], [], [], []
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
    print(solution(N, A, B, C, D))
