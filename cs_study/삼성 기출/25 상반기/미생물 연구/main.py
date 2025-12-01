"""
[좌표 평면]
- 좌측 하단 좌표 0,0 -> 우측 상단 N, N
- 직사각형

[단계]
1. 미생물 투입
2. 배양 용기 이동
3. 실험 결과 기록

[미생물 투입]
1. 투입, 이미 미생물이 존재하면 새로 투입된 미생물이 그 영역만큼 잡아먹음
2. 이전 미생물의 영역이 2개로 나눠지면 모두 사라짐

[배양 용기 이동]
1. 기존 용기의 크기가 동일함, 모든 미생물에 대하여 반복
    - 가장 영역이 큰 무리 선택, 여러 개면 먼저 투입된 순서 기준
    - 선택된 무리를 새 용기에 옮기면서, 기존 형태 유지 목표
        - 용기 범위 벗어나지 않아야 함
        - 다른 미생물 영역과 겹치지 않아야 함
    - x 좌표가 최대한 작은 위치로 옮기되, 그런 좌표가 두개면 y좌표가 작은 것 기준
    - 어떤 곳으로도 이동 불가면 그 미생물 삭제

[실험 결과 기록]
1. 상하좌우로 맞닿은 면이 있는 무리끼리는 인접한 무리
    - 맞닿은 면이 여러 개여도 한 쌍 취급
    - 여러 인접한 무리들에 대한 각 미생물 영역의 곱의 합

"""
from collections import deque
from pprint import pprint
def solution(N, Q, virus_dict):
    virus_map = [[0] * N for _ in range(N)]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    virus_size = {}
    virus_loc = {}
    virus_sticker = {}

    def input_virus(virus_info, idx):
        virus_r1, virus_c1, virus_r2, virus_c2 = virus_info

        # 배치
        for y in range(virus_r1, virus_r2):
            for x in range(virus_c1, virus_c2):
                virus_map[y][x] = idx
            if not virus_sticker.get(idx):
                virus_sticker[idx] = []

            virus_sticker[idx].append(virus_map[y][virus_c1:virus_c2])

        print("before input")
        pprint(virus_map)

        # 마지막꺼는 그대로 들어오므로 사이즈 보존
        virus_size[idx] = (virus_r2 - virus_r1) * (virus_c2 - virus_c1)
        virus_loc[idx] = [virus_r1, virus_c1]

        # 기존 것이 쪼개지는 지 확인
        # 이전 것까지만 계산
        for check_idx in range(1, idx):
            queue = deque()
            visited = [[False]*N for _ in range(N)]
            check_flag = False
            max_size = 0

            # 어딧는 지 모르므로, 찾아야함
            for r in range(N):
                for c in range(N):
                    if visited[r][c]:
                        continue

                    if virus_map[r][c] == check_idx:
                        if not check_flag:
                            virus_loc[check_idx] = [r, c]
                            check_flag = True
                            queue.append((0, r, c))

                            while queue:
                                size, start_y, start_x = queue.popleft()
                                visited[start_y][start_x] = True
                                if max_size < size:
                                    max_size = size

                                for dy, dx in directions:
                                    ny, nx = start_y+dy, start_x+dx
                                    if 0 <= ny < N and 0 <= ny < N and not visited[ny][nx] and virus_map[r][c] == check_idx:
                                        visited[ny][nx] = True
                                        queue.append((size+1, ny, nx))

                            virus_size[check_idx] = max_size
                            # 바이러스 자체를 스티커화시켜서 0,0부터 붙여서 생각하도록 유도
                            total_line = []
                            for i in range(N):
                                new_line = []
                                for j in range(N):
                                    if virus_map[i][j] == check_idx:
                                        new_line.append(virus_map[i][j])

                                if new_line:
                                    total_line.append(new_line)

                            virus_sticker[check_idx] = total_line

                        else:
                            # 두번 찾은 것으로 쪼개진 것을 의미
                            # 해당 인덱스 모두 삭제
                            for a in range(N):
                                for b in range(N):
                                    if virus_map[a][b] == check_idx:
                                        virus_map[a][b] = 0

                            # 사이즈, 위치, 스티커 삭제
                            del virus_size[check_idx]
                            del virus_loc[check_idx]
                            del virus_sticker[check_idx]




    # 영역이 넓은 순으로 x -> y 순으로 배치
    def move_virus():
        # 가장 큰 무리 판별
        size_list = list(virus_size.items())
        size_list.sort(key=lambda x:(-x[1]))

        # 새 맵 생성
        new_map = [[0]*N for _ in range(N)]

        # r, c는 평행이동 변수로 고려
        # 용기 이동
        for virus_idx, _ in size_list:
            y, x = virus_loc[virus_idx]
            is_build = False


        return new_map


    for virus_idx, virus_info in virus_dict.items():
        input_virus(virus_info, virus_idx)
        print("after input")
        pprint(virus_map)
        print("virus_size", virus_size)
        print("virus_loc", virus_loc)
        print("virus_sticker", virus_sticker)

        # print("before move")
        # pprint(virus_map)
        # new_map = move_virus()
        # virus_map = new_map
        # print("after move")
        # pprint(virus_map)
        print()




if __name__ == "__main__":
    N, Q = map(int, input().split())
    virus_dict = {}
    for i in range(Q):
        r1, c1, r2, c2 = map(int, input().split())
        virus_dict[i+1] = [c1, r1, c2, r2]

    solution(N, Q, virus_dict)
