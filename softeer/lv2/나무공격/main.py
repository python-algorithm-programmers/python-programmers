from collections import deque

def attack(m, map_list, l_start, r_end, cnt):
    for row in range(l_start-1, r_end):
        for col in range(m):
            # 환경 파괴 범이 있을 경우
            if map_list[row][col] == 1:
                map_list[row][col] = 0
                cnt -= 1
                break

    return map_list, cnt


def solution(n,m,map_list,l1,r1,l2,r2,cnt):
    udt_map_list, udt_cnt = attack(m, map_list, l1, r1, cnt)
    final_map, final_cnt = attack(m, udt_map_list, l2, r2, udt_cnt)
    return final_cnt



if __name__ == "__main__":
    import sys
    n, m = map(int, sys.stdin.readline().split())

    # 행렬
    map_list = []
    cnt = 0
    for i in range(n):
        lines = list(map(int, sys.stdin.readline().split()))
        # 헌터 수 세기
        for number in lines:
            if number == 1:
                cnt += 1
        map_list.append(lines)

    # 공격
    l1, r1 = map(int, sys.stdin.readline().split())
    l2, r2 = map(int, sys.stdin.readline().split())

    print(solution(n,m,map_list,l1,r1,l2,r2,cnt))
