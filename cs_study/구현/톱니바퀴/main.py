from collections import deque
def solution(K, maps, rotate_d):
    for pers in rotate_d:
        rotate_idx, rotate_dir = pers

        # 톱니바퀴별 회전 방향저장, 입력할 바퀴에 회전방향은 지금 결정
        dirs = [0]*4
        dirs[rotate_idx] = rotate_dir

        # 왼 -> 우로 확장
        right_dir = rotate_dir
        for i in range(rotate_idx, 3):
            if maps[i][2] != maps[i+1][6]:
                right_dir *= -1
                dirs[i+1] = right_dir
            # 바퀴가 같아버리면 종료
            else:
                break

        # 왼 <- 우로 확장
        left_dir = rotate_dir
        for j in range(rotate_idx, 0, -1):
            if maps[j][6] != maps[j-1][2]:
                left_dir *= -1
                dirs[j-1] = left_dir
            # 바퀴가 같아버리면 종료
            else:
                break

        # 한번에 모았다가 회전
        for i in range(4):
            if dirs[i] != 0:
                maps[i].rotate(dirs[i])

    # 점수 매기기
    result = 0
    for i in range(4):
        if maps[i][0] == 1:
            result += 2**i

    return result


if __name__ == "__main__":
    maps = []
    for _ in range(4):
        maps.append(deque(list(map(int, list(input())))))
    K = int(input())
    rotate_d = []
    for _ in range(K):
        int_list = list(map(int, input().split()))
        rotate_d.append([int_list[0]-1, int_list[1]])

    print(solution(K, maps, rotate_d))
