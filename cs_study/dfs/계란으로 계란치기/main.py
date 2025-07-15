def dfs(idx, egg_queue, score, best):
    # 큐를 popleft로 빼지 않고 원래 인덱스를 유지할 수 있도록 함
    # 종료 조건
    # 아예 오른쪽으로 왔을 때
    if idx == len(egg_queue):
        best[0] = max(score, best[0])
        return

    # 현재 인덱스의 계란 깨져있을 때
    if egg_queue[idx][0] <= 0:
        dfs(idx+1, egg_queue, score, best)
        return

    # for문으로 한바퀴 돌면서 다른 계란들을 순환
    # 이때, 손에 든 계란을 한번만 쳐야하므로 치고 나면 바로 다음 인덱스의 dfs 적용
    hit = False
    for j in range(len(egg_queue)):
        plus_score = 0
        # 자기 자신은 칠 수 없으므로
        if j != idx and egg_queue[j][0] > 0:
            # 깨트릴 게 있을 때 설정
            hit = True

            # 내구도 감소
            egg_queue[j][0] -= egg_queue[idx][1]
            egg_queue[idx][0] -= egg_queue[j][1]

            # 다른 계란 깨트릴 때
            if egg_queue[j][0] <= 0:
                plus_score += 1

            # 손에 든 계란도 깨질 때
            if egg_queue[idx][0] <= 0:
                plus_score += 1

            dfs(idx+1, egg_queue, score+plus_score, best)

            # 백트레킹, 참조 변수이기에
            egg_queue[j][0] += egg_queue[idx][1]
            egg_queue[idx][0] += egg_queue[j][1]

    # 깨트릴 계란 없을 때
    if not hit:
        dfs(idx+1, egg_queue, score, best)

def solution(egg_queue):
    best = [0]
    dfs(0, egg_queue, 0, best)
    return best[0]

if __name__ == "__main__":
    N = int(input())
    egg_queue = []
    for _ in range(N):
        endure, weight = map(int, input().split())
        egg_queue.append([endure, weight])
    print(solution(egg_queue))