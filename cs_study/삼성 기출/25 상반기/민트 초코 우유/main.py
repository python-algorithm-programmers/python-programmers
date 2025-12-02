from collections import deque
from pprint import pprint

def solution(N, T, student_map_dict):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    represents = []
    group_order = {
        ('T',): 1,
        ('C',): 2,
        ('M',): 3,
        ('C', 'M',): 4,
        ('M', 'T',): 5,
        ('C', 'T',): 6,
        ('C', 'M', 'T',): 7,
    }

    # 아침 시간
    def morning():
        for r in range(N):
            for c in range(N):
                student_map_dict[(r,c)]["b"] += 1

    # 점심 시간
    """
    1. 그룹 탐색 -> bfs, 신봉 음식이 같은 경우에 대한
    2. 그룹 내 대표자 선출 (b, r, c 기준)
    3. 그룹에서 대표자에게 1씩 걷어서 전달
    4. 대표자 그룹 변수 변경 (set -> key, b,r,c -> value)
    """
    def lunch():
        # 각 그룹내 대표 선출
        visited = [[False]*N for _ in range(N)]
        groups = {}
        for r in range(N):
            for c in range(N):
                if not visited[r][c]:
                    group_f = student_map_dict[(r,c)]["f"]
                    group_b = student_map_dict[(r,c)]["b"]

                    # group_id 세팅
                    group_id = group_f.copy()
                    r_c = f"{r}_{c}"
                    group_id = sorted(list(group_id))
                    group_id.append(r_c)
                    group_id = tuple(group_id)
                    #print(group_id)

                    # 튜플화
                    group_f = tuple(sorted(list(group_f)))
                    groups[group_id] = []
                    queue = deque([(r,c)])
                    groups[group_id].append((group_b, r, c))
                    while queue:
                        start_y, start_x = queue.popleft()
                        visited[start_y][start_x] = True
                        for dy, dx in directions:
                            ny, nx = start_y+dy, start_x+dx
                            if 0 <= ny < N and 0 <= nx < N \
                                and not visited[ny][nx] \
                                and tuple(student_map_dict[(ny,nx)]["f"]) == group_f:
                                groups[group_id].append((student_map_dict[(ny,nx)]["b"], ny, nx))
                                queue.append((ny, nx))
                                visited[ny][nx] = True

                    groups[group_id].sort(key=lambda x:(-x[0], x[1], x[2]))

        # 대표에게 신앙심 전달
        # 대표 외에 나머지 빼고 -> 대표에게 전달
        #print("groups", groups)
        group_keys = groups.keys()
        for group_key in group_keys:
            g_size = len(groups[group_key])
            add_b = 0

            # 대표 빼고 나머지 -1
            for i in range(1, g_size):
                b, r, c = groups[group_key][i]
                student_map_dict[(r,c)]["b"] -= 1
                add_b += 1

            # 대표에게 전달
            _, repr_r, repr_c = groups[group_key][0]
            student_map_dict[(repr_r, repr_c)]["b"] += add_b
            repr_b = student_map_dict[(repr_r, repr_c)]["b"]
            repr_f = student_map_dict[(repr_r, repr_c)]["f"]

            # 대표 등록
            repr_f = list(repr_f)
            repr_f.sort()
            repr_f = tuple(repr_f)
            represents.append((repr_f, repr_b, repr_r, repr_c))

    def dinner():
        """
        [그룹 순서대로 진행]
        1. 단일 음식 - 민트[T], 초코[C], 우유[M]
        2. 이중 - {C,M}, {T,M}, {T,C}
        3. 삼중 - {T, C, M}

        """
        # repr_list = list(represents.items())
        # repr_list.sort(key=lambda x: (len(x[0]), -x[1][0], x[1][1], x[1][2]))

        represents.sort(key=lambda x:(len(x[0]), -x[1], x[2], x[3]))
        #visited = [[False]*N for _ in range(N)]
        #print("repr_list", represents)

        # 전파 예외 대상
        defensive_set = set()
        for repr_f, b, r, c in represents:
            # 전파 예외 대상에 포함되었는 지 확인
            #print("defensive_set", defensive_set)
            if (r, c) in defensive_set:
                continue

            repr_dir = b % 4
            str_x = b - 1
            student_map_dict[(r, c)]["b"] = 1

            # 대표자의 신봉 음식
            repr_f = list(repr_f)
            repr_f.sort()
            repr_f = tuple(repr_f)
            repr_f_set = student_map_dict[(r, c)]["f"].copy()

            """
            간절함 전파
            """
            queue = deque([(r, c)])
            while queue:
                start_y, start_x = queue.popleft()
                dy, dx = directions[repr_dir]
                ny, nx = start_y+dy, start_x+dx

                if 0 <= ny < N and 0 <= nx < N:
                    # 신봉 음식이 같은 경우는 그냥 탐색
                    if tuple(sorted(list(student_map_dict[(ny, nx)]["f"]))) == repr_f:
                        queue.append((ny, nx))

                    # 다른 경우는 전파 진행
                    else:
                        defensive_set.add((ny, nx))
                        stu_y = student_map_dict[(ny, nx)]["b"]

                        # 강한 전파, 같은 음식 신봉, 간절함이 깎임
                        if str_x > stu_y:
                            student_map_dict[(ny, nx)]["f"] = repr_f_set
                            student_map_dict[(ny, nx)]["b"] += 1

                            str_x -= (stu_y+1)
                            if str_x == 0:
                                pass

                            # 간절함이 남은 경우
                            else:
                                queue.append((ny, nx))

                        # 약한 전파
                        else:
                            new_f = repr_f_set.union(student_map_dict[(ny, nx)]["f"].copy())
                            student_map_dict[(ny, nx)]["f"] = new_f

                            # 전파자 간절함 0, 대상의 신앙심은 x만큼 늘어남
                            student_map_dict[(ny, nx)]["b"] += str_x
                            str_x = 0

            #print(f"{repr_f}, ({r},{c})")
            #pprint(student_map_dict)
    def record():
        groups = {}
        for group_key in group_order.keys():
            groups[group_key] = 0

        for i in range(N):
            for j in range(N):
                f_set = student_map_dict[(i, j)]["f"]
                b = student_map_dict[(i, j)]["b"]

                f_set = list(f_set)
                f_set.sort()
                f_tuple = tuple(f_set)
                groups[f_tuple] += b

        # 정렬
        groups_list = list(groups.items())
        groups_list.sort(key=lambda x:-group_order[x[0]])
        #print("groups_list", groups_list)

        # 값만 뽑아내기
        answer = []
        for _, group_b in groups_list:
            answer.append(group_b)

        return answer


    for _ in range(T):
        #print("before morning")
        #pprint(student_map_dict)

        morning()
        #print("after morning")
        #pprint(student_map_dict)

        #print("before lunch")
        #pprint(student_map_dict)

        #print("after lunch")
        lunch()
        #pprint(student_map_dict)
        #print("represents", represents)

        #print("before dinner")
        #pprint(student_map_dict)

        #print("during dinner")
        dinner()

        #print("after dinner")
        #pprint(student_map_dict)

        answer = record()
        print(*answer)

        # 대표자 초기화
        represents = []


if __name__ == "__main__":
    N, T = map(int, input().split())
    # Map 안에 dict 만들기
    student_map_dict = {}
    for i in range(N):
        input_list = list(input())
        for j in range(N):
            student_map_dict[(i, j)] = {}
            student_map_dict[(i, j)]["f"] = set()
            student_map_dict[(i, j)]["f"].add(input_list[j])
    for i in range(N):
        input_list = list(map(int, input().split()))
        for j in range(N):
            student_map_dict[(i,j)]["b"] = input_list[j]

    solution(N, T, student_map_dict)


