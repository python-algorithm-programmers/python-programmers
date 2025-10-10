"""
거리가 1인 경우는 그냥 붙어있는 것이라 return 0
거리가 2인 경우에서 r=1, c=1인 경우는 좌, 우 2가지 모두 파티션이 있는 지 확인
r=2 or c=2이면 그 사이에 파티션이 있는 지만 확인
0. 거리 구하는 함수 구현 -> directions와 같이 1인 경우, 2-1. 2칸씩 2-2. 1칸 1칸씩 대각선 -> dictionary_items 
1. P의 위치 확인해서 위치 저장하는 queue 생성후, 3중 for문으로 그안에 도달하는 P들 찾기
2. 찾은 P들이 조건에 맞게 
"""
from collections import deque


def check_p(queue, dis_dict, place):
    for k, directions in dis_dict.items():
        visited = [[False] * 5 for _ in range(5)]

        for r, c in queue:
            check_q = deque([(r, c)])
            while check_q:
                y, x = check_q.popleft()
                visited[y][x] = True

                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if k == 0:
                        if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx]:
                            if place[ny][nx] == "P":
                                return 0

                    elif k == 1:
                        if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx]:
                            if place[ny][nx] == "P":
                                # 다가오는 사이 간격 확인
                                if dy != 0:
                                    by = y + dy // 2
                                    if place[by][nx] == "X":
                                        visited[ny][nx] = True
                                        check_q.append((ny, nx))
                                    else:
                                        print(place)
                                        print(ny, nx)
                                        print(by, x)
                                        print(y, x)
                                        print(place[by][nx])
                                        print()
                                        return 0


                                elif dx != 0:
                                    bx = x + dx // 2
                                    if place[ny][bx] == "X":
                                        visited[ny][nx] = True
                                        check_q.append((ny, nx))

                                    else:
                                        print(place)
                                        print(ny, nx)
                                        print(ny, bx)
                                        print(place[ny][bx])
                                        print()
                                        return 0

                    # 1, 1씩으로 다가오는 경우 고려
                    else:
                        if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx]:
                            flag = False
                            if place[ny][nx] == "P":
                                if place[ny][x] != "X":
                                    return 0

                                if place[y][nx] != "X":
                                    return 0

                                visited[ny][nx] = True
                                check_q.append((ny, nx))

    return 1


def solution(places):
    dis_dict = {
        0: [(0, -1), (0, 1), (-1, 0), (1, 0)],
        1: [(-2, 0), (0, -2), (2, 0), (0, 2)],
        2: [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    }
    # P 위치만 먼저 저장, 단계별로 처리
    answer = []
    for place in places:
        queue = deque()
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    queue.append((i, j))

        answer.append(check_p(queue, dis_dict, place))

    return answer