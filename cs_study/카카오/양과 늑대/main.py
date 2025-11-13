from collections import deque


def solution(info, edges):
    visited = [False] * len(info)
    visited[0] = True
    adj = {node: [] for node in range(len(info))}

    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    best = [0]

    def dfs(goat, wolf, candidates):
        print(candidates)
        best[0] = max(best[0], goat)
        for cur in list(candidates):
            new_goat = goat
            new_wolf = wolf
            if info[cur] == 0:
                new_goat = goat + 1
            else:
                new_wolf = wolf + 1

            if new_goat <= new_wolf:
                continue

            new_candidates = candidates.copy()
            new_candidates.remove(cur)
            for nxt in adj[cur]:
                if not visited[nxt]:
                    new_candidates.add(nxt)

            visited[cur] = True
            dfs(new_goat, new_wolf, new_candidates)
            visited[cur] = False

    dfs(1, 0, set(adj[0]))
    return best[0]

if __name__ == "__main__":
    info = [0,1,0,1,1,0,1,0,0,1,0]
    edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
    print(solution(info, edges))