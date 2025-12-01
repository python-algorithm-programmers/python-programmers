from collections import deque
from pprint import pprint
class Colony:
    def __init__(self, first, size):
        self.first = first
        self.loc = []
        self.sticker = []
        self.size = size
    def __repr__(self):
        return f"Colony(first={self.first}, loc={self.loc}. sticker={self.sticker}, size={self.size})"

    def update_size(self, size):
        self.size = size

    def update_sticker(self, sticker):
        self.sticker = sticker

    def update_loc(self, loc):
        self.loc = loc



def solution(N, Q, colony_dict):
    virus_map = [[0]*N for _ in range(N)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    index_set = set()
    """
    [필요한 인자]
    - 새로 투입되는 colony, virus_map
    
    [수행 내용]
    1. 새 미생물 군집 투입 -> 기존것에 덮어씀
        - 기존 것이 두 무리로 나뉘면 사라짐
    2. 현재 군집의 형태를 담은 스티커, 사이즈, 시작 위치 저장
    """
    def input_colony(input_idx):
        colony = colony_dict[input_idx]

        # 새 미생물 군집 투입
        r1, c1, r2, c2 = colony.first
        total_line = []
        for r in range(r1, r2):
            for c in range(c1, c2):
                virus_map[r][c] = input_idx
            total_line.append(virus_map[r][c1:c2])

        # 현재 군집의 형태, 사이즈, 시작 위치 저장
        colony.update_size((r2-r1)*(c2-c1))
        colony.update_sticker(total_line)
        colony.update_loc([r1,c1])

        # 이전 인덱스에 대해 분리되는 지 조사
        # 그러면서 변경된 사이즈와 스터커로 업데이트
        index_list = list(index_set)
        for past_idx in index_list:
            visited = [[False]*N for _ in range(N)]
            past_colony = colony_dict[past_idx]
            y, x = past_colony.loc
            component_cnt = 0

            # 스티커 바꾸기
            # 사이즈도 조사하기
            # 덮어씌어졌는 지 여부도 확인
            is_over = True
            for i in range(N):
                for j in range(N):
                    if virus_map[i][j] == past_idx and not visited[i][j]:
                        component_cnt += 1
                        is_over = False
                        queue = deque([(i, j)])
                        cur_size = 0
                        while queue:
                            start_y, start_x = queue.popleft()
                            cur_size += 1
                            visited[start_y][start_x] = True

                            for dy, dx in directions:
                                ny, nx = start_y+dy, start_x+dx
                                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and virus_map[ny][nx] == past_idx:
                                    queue.append((ny, nx))
                                    visited[ny][nx] = True

                        # 사이즈, 스티커 바꾸기
                        past_colony.update_size(cur_size)
                        # 좌표로 기억
                        cells = []
                        for a in range(N):
                            for b in range(N):
                                if virus_map[a][b] == past_idx:
                                    cells.append((a, b))

                        # 경계 확보
                        min_r = min(r for r, _ in cells)
                        max_r = max(r for r, _ in cells)
                        min_c = min(c for _, c in cells)
                        max_c = max(c for _, c in cells)

                        # 여백 포함해서 sticker 크기 만들기
                        h = max_r - min_r + 1
                        w = max_c - min_c + 1
                        sticker = [[0]*w for _ in range(h)]

                        for r, c in cells:
                            sticker[r-min_r][c-min_c] = past_idx

                        past_colony.update_sticker(sticker)
                        past_colony.update_loc([min_r, min_c])

            # 못 찾은 거면, 들어올 때 아예 덮어씌어진 경우
            if is_over:
                del colony_dict[past_idx]
                index_set.remove(past_idx)

            # flag가 True이면 분리된 것
            # map에서 삭제, colony_dict도 삭제
            if component_cnt >= 2:
                del colony_dict[past_idx]
                index_set.remove(past_idx)
                for a in range(N):
                    for b in range(N):
                        if virus_map[a][b] == past_idx:
                            virus_map[a][b] = 0

        # 새로 추가할 인덱스 넣기
        index_set.add(input_idx)

    def move():
        candidate = []
        colony_list = list(colony_dict.items())
        colony_list.sort(key=lambda x:(-colony_dict[x[0]].size, x[0]))
        for idx, colony in colony_list:
            if colony.sticker:
                candidate.append([idx, colony.sticker, colony.loc])

        # 배양 용기에 있는 미생물 이동
        new_map = [[0]*N for _ in range(N)]
        for colony_idx, sticker, loc in candidate:
            can_build = False

            for c in range(N):
                if can_build: break
                for r in range(N):
                    if can_build: break
                    # 붙이기 전에 옮길 수 있는 지 확인
                    # 여기 기준으로 미생물 붙이다가 안되면, 다음 곳으로 이동
                    can_stick = True
                    if new_map[r][c] == 0 or sticker[0][0] == 0:
                        for y in range(len(sticker)):
                            if not can_stick: break
                            for x in range(len(sticker[y])):
                                if y+r >= N or x+c >= N:
                                    can_stick = False
                                    break
                                if new_map[y+r][x+c] != 0 and sticker[y][x] != 0:
                                    can_stick = False
                                    break

                        if can_stick:
                            # 새로 시작 점 지정
                            colony_dict[colony_idx].update_loc([r, c])
                            for y in range(len(sticker)):
                                for x in range(len(sticker[y])):
                                    # 공백 고려
                                    if sticker[y][x] != 0:
                                        new_map[y+r][x+c] = sticker[y][x]
                            can_build = True

        return new_map

    def calculate():
        # 인접한 지 여부 판단
        index_list = list(index_set)
        adj_dict = {}
        for colony_idx in index_list:
            y, x = colony_dict[colony_idx].loc
            adj_dict[colony_idx] = []
            visited = [[False]*N for _ in range(N)]
            add_colony_set = set()
            queue = deque([(y, x)])
            while queue:
                start_y, start_x = queue.popleft()
                visited[start_y][start_x] = True
                for dy, dx in directions:
                    ny, nx = start_y+dy, start_x+dx
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                        # 다른 영역의 것이면 근접 set으로 추가
                        if virus_map[ny][nx] != colony_idx:
                            if virus_map[ny][nx] != 0:
                                add_colony_set.add(virus_map[ny][nx])
                                visited[ny][nx] = True
                        else:
                            queue.append((ny, nx))
                            visited[ny][nx] = True

            # 근접한 것을 찾으면 쌍으로 묶기
            for colony_data in add_colony_set:
                adj_dict[colony_idx].append(colony_data)

        # 인접해서 둘다 포함된 경우이니 나누기 2해주기
        answer = 0
        for idx, adj_idx_list in adj_dict.items():
            for other_idx in adj_idx_list:
                answer += colony_dict[idx].size * colony_dict[other_idx].size

        answer //= 2
        return answer

    # 여기서 작업을 반복
    for idx in range(1, Q+1):
        #print("before input")
        #pprint(virus_map)
        input_colony(idx)
        #print("after input")
        #pprint(virus_map)
        #print("colony", colony_dict)

        #print("before move")
        #pprint(virus_map)
        new_map = move()
        virus_map = new_map
        #print("after move")
        #pprint(virus_map)
        #print("colony", colony_dict)
        answer = calculate()
        print(answer)


if __name__ == "__main__":
    N, Q = map(int, input().split())
    colony_dict = {}
    for i in range(1, Q+1):
        c1, r1, c2, r2 = map(int, input().split())
        colony = Colony([r1, c1, r2, c2], (r2-r1)*(c2-c1))
        colony_dict[i] = colony
    solution(N, Q, colony_dict)