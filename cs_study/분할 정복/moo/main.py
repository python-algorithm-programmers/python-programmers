"""
목표: N이 어느 partition 범위 안에 들어왔는 지 top -> bottom 식으로 찾기
partition: s(k)나 s(k-1)의 시작과 끝 범위
S(0) = "moo"
S(k) = S(k-1) + "m" + "o"*(k+2) + S(k-1)

과정:
1. dfs로 분할: 어느 범위에 속한 지 파악
2. 작은 범위에서만 문자열로 찾기: 어떠한 partition인 지 찾으면 거기서만 문자열 구성해서 인덱스로 찾기
"""

def bisect_dfs(depth, length, N):
    if depth == 0:
        return "moo"[N-1]

    left_len = length[depth - 1]
    center_len = depth + 3

    # [분할]
    # 왼쪽 영역
    if N <= left_len:
        # [정복] 더 작은 문제인 S(k-1) 안으로 재귀
        return bisect_dfs(depth-1, length, N)

    # 센터
    elif left_len < N <= left_len + center_len:
        if N - left_len == 1:
            # [결합], 결과물이 최종으로 합쳐지진 않지만 분할된 결과를 조합해서 얻긴 함
            return "m"

        else:
            return "o"

    # 오른쪽 영역
    else:
        last_len = N - (left_len + center_len)
        return bisect_dfs(depth-1, length, last_len)


def solution(N):
    # N이 인덱스에 포함될때까지 length 배열에 추가
    # length 배열은 depth에 따른 문자열 길이를 저장한 리스트
    length = [3]
    while length[-1] < N:
        depth = len(length)
        length.append(length[-1]*2 + depth+3)

    return bisect_dfs(len(length)-1, length, N)


if __name__ == "__main__":
    N = int(input())
    print(solution(N))
