from collections import deque

def bfs(start, groups, visited):
    queue = deque([start])
    cnt = 1 # 시작 노드 포함
    visited[start] = True
    while queue:
        node_index = queue.popleft()
        for neighbor in groups[node_index]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                cnt += 1
    return cnt

def solution(n, wires):
    # 0번째 버리고 인덱스로 리스트 적용
    min_group_cnt = n
    for i in range(n):
        temp_wires = wires[:i] + wires[i+1:]
        groups = [[] for _ in range(n+1)]
        for a, b in temp_wires:
            groups[a].append(b)
            groups[b].append(a)

        visited = [False]*(n+1)
        group_cnt = bfs(1,groups,visited)
        diff = n - group_cnt*2
        min_group_cnt = min(min_group_cnt, abs(diff))
    return min_group_cnt

if __name__ == "__main__":
    n = 9
    wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    print(solution(n, wires))