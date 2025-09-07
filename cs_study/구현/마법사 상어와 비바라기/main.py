if __name__ == "__main__":
    N, M = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))

    water_magic = []
    for _ in range(M):
        water_magic.append(list(map(int, input().split())))
    water_magic.sort(key=lambda x:-x[1])
    extend_cnt = water_magic[0][1] // N + 2

    # 최대 움직임 기반 확장
    new_maps = []
    for i in range(N):
        new_maps.append(maps[i]*extend_cnt)
    real_maps = []
    for _ in range(extend_cnt):
        real_maps.extend(new_maps[:])
    print(real_maps)