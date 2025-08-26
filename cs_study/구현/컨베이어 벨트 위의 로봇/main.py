from collections import deque


def solution(N, K, robot_belts):
    # 벨트 큐, 내구도와 인덱스를 갖고 있음
    robot_belts_q = deque(robot_belts)
    turn_cnt = 0

    while True:
        turn_cnt += 1

        # 벨트 이동
        robot_belts_q.rotate(1)

        # 로봇 내리는 위치에 있는 지 확인하고 있으면 내리기
        if robot_belts_q[N - 1][1]:
            robot_belts_q[N - 1][1] = False

        # 벨트에 올라간 로봇 이동
        # 내리는 곳 빼고 조사 -> 어짜피 내리는 곳 전에는 모두
        for i in range(N-2, -1, -1):
            # 이전 벨트에 로봇이 있고빈 벨트이고 내구도 있는 지 확인 후 이동
            if robot_belts_q[i][1] \
                    and not robot_belts_q[i+1][1] \
                    and robot_belts_q[i+1][0] > 0:

                robot_belts_q[i+1][1] = True
                robot_belts_q[i+1][0] -= 1
                robot_belts_q[i][1] = False

        # 로봇 내리는 위치에 있는 지 확인하고 있으면 내리기
        if robot_belts_q[N-1][1]:
            robot_belts_q[N - 1][1] = False

        # 로봇 올리는 위치에 올리고, 내구도 깎기
        if robot_belts_q[0][0] > 0 and not robot_belts_q[0][1]:
            robot_belts_q[0][1] = True
            robot_belts_q[0][0] -= 1

        # 내구도 확인
        zero_cnt = sum(1 for q in robot_belts_q if q[0] == 0)
        if zero_cnt == K:
            return turn_cnt

if __name__ == "__main__":
    N, K = map(int, input().split())
    belts = list(map(int, input().split()))
    robot_belts = [[belt, False] for belt in belts]
    print(solution(N, K, robot_belts))