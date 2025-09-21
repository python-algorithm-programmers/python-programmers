from collections import deque
def networkOptimization(numRegions, numConnections, numTypes, fromRegion, toRegion, connectionType):
    # 타입별 간선 분리
    adj_t = [[] for _ in range(numTypes)]
    adj_set = {}
    for i in range(numConnections):
        t = connectionType[i]
        adj_t[t].append((fromRegion[i], toRegion[i]))
        # 타입별, 존재하는 노드만 색출
        adj_set.setdefault(t, set()).add(fromRegion[i])
        adj_set.setdefault(t, set()).add(toRegion[i])

    # 타입별로 지나갔는 지 확인
    result = [0] * numTypes
    for t in range(numTypes):
        components = 0 # 최소 간선 수만 파악
        edge_line = 0
        adj = [[] for _ in range(numRegions)]
        # 인접 행렬로 지나가는 노드 확보
        for u, v in adj_t[t]:
            adj[u].append(v)
            adj[v].append(u)

        # 같은 타입으로된 네트워크 노드들 한해서만 탐색
        visited = [False] * numRegions
        for node in adj_set[t]:
            # 이 visited가 중복 방문을 배제함
            if not visited[node]:
                # 여기서 while 문 탈출하면 그건 또다른 뭉텅이
                components += 1
                visited[node] = True
                queue = deque([node])
                while queue:
                    cur = queue.popleft()
                    for nxt in adj[cur]:
                        if not visited[nxt]:
                            queue.append(nxt)
                            visited[nxt] = True
                            edge_line += 1

        if components == 1:
            result[t] = edge_line
        # 연결이 여러 군데라 없는 것
        else:
            result[t] = 0

    return result

if __name__ == "__main__":
    numRegions = 4
    numConnections = 5
    numTypes = 2
    fromRegion = [3, 0, 0, 2, 1]
    toRegion = [2, 3, 2, 1, 3]
    connectionType = [1, 0, 0, 1, 1]
    print(networkOptimization(numRegions, numConnections, numTypes, fromRegion, toRegion, connectionType))