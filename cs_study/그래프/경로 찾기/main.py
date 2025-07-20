def solution(N, maps):
    transition_flag = True
    while transition_flag:
        transition_flag = False
        for y in range(N):
            for x in range(N):
                if maps[y][x] == 1:
                    continue
                # 3중 for문
                # 중간 매개체가 있으면 연결된 것이므로 매개체를 찾기
                for z in range(N):
                    # 애초에 연결된 것이면 다음 것으로 넘기기
                    if maps[y][z] == 1 and maps[z][x] == 1:
                        maps[y][x] = 1
                        transition_flag = True
                        break
    return maps


if __name__ == "__main__":
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    answer = solution(N, maps)
    for row in answer:
        print(*row)