def solution(N, M, trees):
    # 이분탐색을 구간이 아니라 높이로 아예둠
    start = 0
    end = trees[0]
    while start <= end:
        # 초기화
        sum_m = 0

        # 합계 계산해서 앞, 뒤 고름
        mid = (start+end)//2
        for i in range(len(trees)):
            left_tree_h = trees[i] - mid
            if left_tree_h > 0:
                sum_m += left_tree_h
            else:
                break

        # 범위 앞, 뒤갈지 선택
        if sum_m == M:
            return mid

        elif sum_m > M:
            start = mid + 1

        else:
            end = mid - 1

    # 못찾으면 -1 반환
    return -1


if __name__ == "__main__":
    import sys
    N, M = map(int, input().split())
    trees = list(map(int, sys.stdin.readline().strip().split()))

    # 오름차순 정렬
    trees.sort(key=lambda x: -x)
    print(solution(N, M, trees))