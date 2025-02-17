def solution(N, distance, test_distance):
    result = [0] * 100
    cur_idx = 0
    test_idx = 0
    for i in range(N):
        cur_dis = distance[i][0] + cur_idx
        for j in range(cur_idx, cur_dis):
            result[j] = distance[i][1]
        cur_idx = cur_dis

    for k in range(N):
        test_dis = test_distance[k][0] + test_idx
        for l in range(test_idx, test_dis):
            result[l] -= test_distance[k][1]
        test_idx = test_dis

    return abs(min(result))

if __name__ == "__main__":
    import sys
    start_list = list(map(int, sys.stdin.readline().strip().split(" ")))
    N, M = start_list[0], start_list[1]

    distance = []
    for i in range(N):
        distance.append(tuple(map(int, sys.stdin.readline().strip().split(" "))))

    test_distance = []
    for i in range(M):
        test_distance.append(tuple(map(int, sys.stdin.readline().strip().split(" "))))

    print(solution(N, distance, test_distance))