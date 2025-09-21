def networkOptimization(numRegions, numConnections, numTypes, fromRegion, toRegion, connectionType):
    # 타입별 간선/노드 모으기
    adj_t = [[] for _ in range(numTypes)]
    adj_set = {}
    for i in range(numConnections):
        t = connectionType[i]
        adj_t[t].append((fromRegion[i], toRegion[i]))
        adj_set.setdefault(t, set()).add(fromRegion[i])
        adj_set.setdefault(t, set()).add(toRegion[i])
    result = [0] * numTypes

    # 루트를 찾는 메서드
    def _find(x, parent):
        if parent[x] != x:
            parent[x] = _find(parent[x], parent)
        return parent[x]

    # 2개의 노드를 합치는 메서드
    def _union(a, b, parent, rank):
        ra, rb = _find(a, parent), _find(b, parent)
        # 이미 연결 여부 확인
        if ra == rb:
            return False

        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1

        return True


    # rank[x]의 정의
    # 노드 x가 루트일 때 그 트리의 추정된 높이
    # 타입별 처리
    for t in range(numTypes):
        parent = list(range(numRegions))
        rank = [0] * numRegions
        edge_line = 0

        # 간선 갯수 세기
        for u, v in adj_t[t]:
            if _union(u, v, parent, rank):
                edge_line += 1

        # 실제로 타입별에 특정 노드가 root 인지 확인
        # root가 단 한개만 있어야 한 뭉텅이
        roots = set(_find(node, parent) for node in adj_set[t])
        if len(roots) == 1:
            result[t] = edge_line
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