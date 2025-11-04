import copy
from collections import deque

def solution(test_cases):
    for case_dict in test_cases:
        print(case_dict)

        indegree_dict = {
            node: 0 for node in range(1, len(case_dict)+1)
        }
        print(indegree_dict)
        for key in indegree_dict:
            for nxt in case_dict.get(key):
                indegree_dict[nxt] += 1

        queue = deque()
        result = []
        for key in indegree_dict:
            if indegree_dict[key] == 0:
                queue.append(key)
                result.append(key)

        if not queue:
            print("IMPOSSIBLE")
            continue

        while queue:
            cur = queue.popleft()
            for nxt in case_dict.get(cur):
                indegree_dict[nxt] -= 1

                if indegree_dict[nxt] == 0:
                    queue.append(nxt)
                    result.append(nxt)
        if len(result) == len(case_dict.keys()):
            print(" ".join(map(str, result)))
        else:
            print("IMPOSSIBLE")


if __name__ == "__main__":
    N = int(input())
    test_cases = []
    for _ in range(N):
        team_len = int(input())
        adj_dict = {
           node: [] for node in range(1, team_len+1)
        }
        team_rank = list(map(int, input().split()))
        # 이 순서대로 의존하도록 결정
        for i in range(len(team_rank)):
            for j in range(i+1, len(team_rank)):
                adj_dict[team_rank[i]].append(team_rank[j])

        change_cycle = int(input())
        for _ in range(change_cycle):
            first, second = map(int, input().split())

            # 간선에 원소가 있는 경우 -> 이 말은 앞선 순위였다는 것을 의미
            if second in adj_dict[first]:
                adj_dict[first].remove(second)
                adj_dict[second].append(first)

            else:
                adj_dict[second].remove(first)
                adj_dict[first].append(second)

        test_cases.append(adj_dict)
    solution(test_cases)


