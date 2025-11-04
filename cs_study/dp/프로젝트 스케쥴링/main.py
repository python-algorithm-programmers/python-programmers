"""
시간이 더 오래 걸린 것만 택하는 방식으로 적용 -> max를 갱신하는 방법으로 적용

[구현]
1. 시작되는 지점에서 부터 찾기
2. 그 다음 순서로 뭐가 진행될 지를 찾는 연결하는 인접 그래프 놓기
3. 각 작업의 완료시간은 '선행 작업 중 가장 오래 걸린 경로' + 자기 작업 시간으로 갱신
"""

def solution(adj, time_dict, start_point):
    indegree_dict = {
        node: 0 for node in time_dict
    }
    for pre in adj:
        for nxt in adj[pre]:
            indegree_dict[nxt] += 1

    print(indegree_dict)
    result_time = {
        node: 0 for node in time_dict
    }

    queue = deque()
    for indegree_node in indegree_dict:
        if indegree_dict[indegree_node] == 0:
            queue.append(indegree_node)
            result_time[indegree_node] = time_dict[indegree_node]

    #print(indegree_dict)
    # 탐색 시작
    while queue:
        cur = queue.popleft()
        for nxt in adj.get(cur, []):
            indegree_dict[nxt] -= 1
            result_time[nxt] = max(result_time[cur] + time_dict[nxt], result_time[nxt])
            if indegree_dict[nxt] == 0:
                queue.append(nxt)

    #print(result_time)
    return max(result_time.values())





if __name__ == "__main__":
    import sys
    from collections import deque

    time_dict = {}
    adj = {}
    start_point = []
    lines = sys.stdin.read().strip().split('\n')
    for line in lines:
        line = line.strip()
        work_line = line.split()
        if len(work_line) == 2:
            first_work, end_date = work_line[0], work_line[1]
            start_point = [first_work, int(end_date)]
            time_dict[first_work] = int(end_date)
        else:
            result_work, end_date, require_works = work_line[0], work_line[1], work_line[2]
            for require in require_works:
                adj.setdefault(require, []).append(result_work)
            time_dict[result_work] = int(end_date)

    print(solution(adj, time_dict, start_point))