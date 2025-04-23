from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque(truck_weights)
    turn = 0
    truck_wg_sum = 0
    road_truck = deque()
    while queue:
        turn += 1
        # 0. turn이 끝난 road_truck은 삭제
        while road_truck:
            if road_truck[0][1] < turn:
                truck_wg_sum -= road_truck[0][0]
                road_truck.popleft()
            else:
                break

        # 1. 다음 큐를 추가 가능 여부 확인
        if truck_wg_sum+queue[0] <= weight:
            truck_weight = queue.popleft()
            truck_wg_sum += truck_weight
            road_truck.append((truck_weight, turn+(bridge_length-1)))

            # 마지막 큐면 리턴
            if not queue:
                return turn+bridge_length

        else:
            first_one = road_truck[0]
            turn = first_one[1]


if __name__ == "__main__":
    bridge_length = 10
    weight = 100
    truck_weights = [50, 30, 10, 10, 30, 10, 40]
    print(solution(bridge_length, weight, truck_weights))