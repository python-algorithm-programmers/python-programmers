from collections import deque


def solution(N,M,K,fb_cms):
    directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    fb_queue = deque((r-1, c-1, m, s, dir_num) for r, c, m, s, dir_num in fb_cms)

    for _ in range(K):
        maps = [[[] for _ in range(N)] for _ in range(N)]
        fb_where = set()

        # 이동
        for _ in range(len(fb_queue)):
            r, c, m, s, dir_num = fb_queue.popleft()
            dy, dx = directions[dir_num]
            ny, nx = r+dy*s, c+dx*s

            # 범위가 넘거나 음수인 경우
            if ny < 0 or ny >= N:
                ny = ny % N
            if nx < 0 or nx >= N:
                nx = nx % N

            maps[ny][nx].append((m, s, dir_num))
            fb_where.add((ny,nx))

        # 2개 이상의 파이어볼인 경우 확인
        for ny, nx in fb_where:
            if len(maps[ny][nx]) == 1:
                m, s, dir_num = maps[ny][nx][0]
                fb_queue.append((ny, nx, m, s, dir_num))

            elif len(maps[ny][nx]) >= 2:
                total_m, total_s = 0, 0
                odd_dir, even_dir = False, False

                for m, s, dir_num in maps[ny][nx]:
                    total_m += m
                    total_s += s
                    if dir_num % 2 == 0:
                        even_dir = True
                    else:
                        odd_dir = True

                # 분배
                div_m = total_m // 5
                # 질량이 0인 파이어볼은 그냥 분해
                if div_m == 0:
                    continue
                div_s = total_s // len(maps[ny][nx])
                if odd_dir and even_dir:
                    total_d = [1,3,5,7]
                else:
                    total_d = [0, 2, 4, 6]

                for i in range(4):
                    fb_queue.append((ny, nx, div_m, div_s, total_d[i]))

    answer = 0
    for _ in range(len(fb_queue)):
        m = fb_queue.popleft()[2]
        answer += m

    return answer

if __name__ == "__main__":
    N,M,K = map(int, input().split())
    fb_cms = []
    for _ in range(M):
        fb_cms.append(list(map(int, input().split())))
    print(solution(N,M,K,fb_cms))