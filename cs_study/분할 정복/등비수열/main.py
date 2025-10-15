"""
1. 분할
a (1 + r + r^2 + ... + r^n)
a mod m * (1 mod m + r mod m + r^2 mod m + .. + r^n mod m)

만약에 1이면 r mod m을 적용함

2. 정복
재귀 함수: r^n 에서 n을 // 2로 적용해서 left, right로 적용

3. return left * right

[구조]
sum_mod()
pow_mod()
"""
def pow_mod(r, n, mod):
    if n == 0:
        return 1
    if n == 1:
        return r % mod

    half = pow_mod(r, n // 2, mod)
    result = (half * half) % mod
    if n % 2 == 1:
        result = ((result % mod) * (r % mod)) % mod

    return result


def sum_mod(r, n, mod):
    if n == 1:
        return 1

    # 짝수
    if n % 2 == 0:
        half = sum_mod(r, n // 2, mod)
        power = pow_mod(r, n // 2, mod)
        return (half * (1 + power)) % mod

    # 홀수
    else:
        return (sum_mod(r, n-1, mod) + pow_mod(r, n-1, mod)) % mod



def solution(a, r, n, mod):
    # a는 마지막에 곱해주기
    a_mod = a % mod
    return (a_mod * sum_mod(r, n, mod)) % mod

if __name__ == "__main__":
    a, r, n, mod = map(int, input().split())
    print(solution(a, r, n, mod))