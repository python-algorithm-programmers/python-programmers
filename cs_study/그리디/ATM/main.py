def solution(members, N):
    members.sort()
    answer = 0
    for i in range(N):
        sum_member = 0
        for j in range(i+1):
            sum_member += members[j]
        answer += sum_member

    return answer

if __name__ == "__main__":
    N = int(input())
    members = list(map(int, input().split()))
    print(solution(members, N))