def solution(N, A, B, C, D):
    # B-C, A-D 합치기
    BC = {}
    AD = {}

    for i in range(N):
        for j in range(N):
            bc = B[i] + C[j]
            ad = A[i] + D[j]
            BC[bc] = BC.get(bc, 0) + 1
            AD[ad] = AD.get(ad, 0) + 1

    # 투 포인터 적용하기 위해 정렬 필수
    BC_list = list(BC.keys())
    AD_list = list(AD.keys())
    BC_list.sort()
    AD_list.sort()
    # print(BC)
    # print(BC_list)
    # print(AD)
    # print(AD_list)
    # print()

    # 1개의 배열에서가 아닌 2개 배열 내에서 투포인터 적용
    # start를 BC에 end를 AD 배열에 적용
    answer = 0
    start, end = 0, len(AD_list) - 1
    while start < len(BC_list) and end >= 0:
        bc_key, ad_key = BC_list[start], AD_list[end]
        sum_bcad = bc_key + ad_key

        if sum_bcad == 0:
            answer += (BC[bc_key] * AD[ad_key])
            start += 1
            # print(start, end)
            # print(BC[bc_key])
            # print(AD[ad_key])
            # print()

        elif sum_bcad > 0:
            end -= 1

        else:
            start += 1

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
