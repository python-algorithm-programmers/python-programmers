def solution(N, M, celebration_members, one_depth_friends):
    # 친구의 친구 찾기
    two_depth_friends = set()
    for members in celebration_members:
        one, two = members
        if one in one_depth_friends:
            two_depth_friends.add(two)
        elif two in one_depth_friends:
            two_depth_friends.add(one)
        else:
            continue
    return len(two_depth_friends | one_depth_friends)

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    celebration_members = []
    one_depth_friends = set()
    for _ in range(M):
        # 1이 포함된 라인은 빨리 카운트 세고 제외
        one, two = map(int, input().split())
        if one == 1:
            one_depth_friends.add(two)
        elif two == 1:
            one_depth_friends.add(one)
        else:
            celebration_members.append((one, two))

    print(solution(N, M, celebration_members, one_depth_friends))
