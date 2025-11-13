from functools import lru_cache

def solution(dist_limit: int, split_limit: int) -> int:
    # 상태: (현재 경로 분배도 P, 현재 깊이에 존재하는 노드 수 n, 남은 분배 노드 수 rem)
    # 선택: 이 깊이에서 k개(1..min(n, rem))를 분배 노드로 만들고, 자식 수 b∈{2,3}를 동일하게 선택
    # 제약: P*b ≤ split_limit (그 자식들이 리프가 될 수 있어야 함)

    @lru_cache(None)
    def dp(P: int, n: int, rem: int) -> int:
        if n == 0:
            return 0
        if P > split_limit:           # 이 깊이의 노드들은 리프가 될 수도, 더 분기할 수도 없음
            return -10**9             # 불가능 상태

        # (1) 이 깊이에서 더 분기하지 않음 → 전부 리프
        best = n

        # (2) 이 깊이에서 분기: 같은 깊이의 분배 노드는 동일한 b(2 또는 3)
        for b in (2, 3):
            if P * b > split_limit:
                continue
            max_k = min(n, rem)
            for k in range(1, max_k + 1):
                # k개만 분배 노드로 사용, 나머지(n-k)는 여기서 리프 확정(P)
                leaves_here = n - k
                leaves_next = dp(P * b, k * b, rem - k)
                best = max(best, leaves_here + leaves_next)

        return best

    # 시작: 루트의 자식 1개가 깊이 1에 존재, 경로 분배도 P=1
    return dp(1, 1, dist_limit)


print(solution(3, 6))    # 6
print(solution(0, 10))   # 1
print(solution(3, 100))  # 7
print(solution(5, 16))   # 9