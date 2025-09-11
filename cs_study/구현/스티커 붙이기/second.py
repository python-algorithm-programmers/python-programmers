def rotate(sticker):
    return [row for row in zip(*sticker[::-1])]
def solution(N,M,K,stickers, sticker_sizes):
    maps = [[0]*M for _ in range(N)]
    for sticker_map, sticker_size in zip(stickers, sticker_sizes):
        turn = 4
        while turn > 0:
            r, c = len(sticker_map), len(sticker_map[0])
            next_flag = True
            break_loop = False
            for y in range(N):
                if break_loop: break
                for x in range(M):
                    # 위 -> 아래, 왼 -> 우로 한칸씩 이동할 때마다 flag 초기화
                    next_flag = True
                    for i in range(r):
                        for j in range(c):
                            if y+i>=N or x+j>=M:
                                next_flag = False
                                break

                            if maps[y+i][x+j] != 0 and sticker_map[i][j] == 1:
                                next_flag = False
                                break

                        if not next_flag:
                            break

                    # 회전 전에 스티커를 붙이는 데 문제가 없었다면, 스티커 붙이고 그대로 종료
                    if next_flag:
                        for i in range(r):
                            for j in range(c):
                                if 0<=y+i<N and 0<=x+j<M and sticker_map[i][j] == 1:
                                    maps[y+i][x+j] = 1

                        break_loop = True
                        break

            # 회전 전에 스티커 붙이면 종료
            if next_flag: break

            # 90도 회전
            sticker_map = rotate(sticker_map)
            turn -= 1

    answer = 0
    answer += sum(sum(row) for row in maps)
    return answer

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    stickers = []
    sticker_size = []
    for _ in range(K):
        r, c = map(int, input().split())
        sticker_size.append((r, c))
        sticker = []
        for _ in range(r):
            sticker.append(list(map(int, input().split())))
        stickers.append(sticker)
    print(solution(N,M,K,stickers, sticker_size))
