import sys
from bisect import bisect_left

def solve_minimax_by_cuts(gap_lengths, ant_cnt):
    num_gaps = len(gap_lengths)
    if num_gaps == 0:
        return 0

    cut_num = ant_cnt - 1
    if cut_num <= 0:              # 않 끊음은 한 구간이니 전체 합
        return sum(gap_lengths)
    if cut_num >= num_gaps:       # 모든 간격을 다 끊으면 각 구간 길이 0
        return 0

    # prefix_sums[j] = gap_lengths[0] + ... + gap_lengths[j-1]
    prefix_sums = [0] * (num_gaps + 1)
    for idx, length in enumerate(gap_lengths):
        prefix_sums[idx + 1] = prefix_sums[idx] + length

    def sum_of_gaps(left_idx: int, right_idx: int) -> int:

        if left_idx > right_idx:
            return 0
        return prefix_sums[right_idx + 1] - prefix_sums[left_idx]

    INF = 10 ** 9
    dp = [[INF] * num_gaps for _ in range(cut_num)]

    # 첫 절단이 last_cut_gap_idx 에서 일어날 때,
    # 첫 구간은 gap_lengths[0 부터 last_cut_gap_idx-1]
    for last_cut_gap_idx in range(num_gaps):
        dp[0][last_cut_gap_idx] = sum_of_gaps(0, last_cut_gap_idx - 1)

    # 두 번째 절단부터 누적
    for cut_order_index in range(1, cut_num):
        for last_cut_gap_idx in range(num_gaps):
            best_max = INF
            # 직전 절단 위치 prev_cut_gap_idx < last_cut_gap_idx
            for prev_cut_gap_idx in range(last_cut_gap_idx):
                new_segment_sum = sum_of_gaps(prev_cut_gap_idx + 1, last_cut_gap_idx - 1)
                candidate_max = max(dp[cut_order_index - 1][prev_cut_gap_idx], new_segment_sum)
                if candidate_max < best_max:
                    best_max = candidate_max
            dp[cut_order_index][last_cut_gap_idx] = 0 if best_max == INF else best_max

    # 마지막 절단을 last_cut_gap_idx 에서 했을 때, 오른쪽 마무리 구간:
    # gap_lengths[last_cut_gap_idx+1 부터 num_gaps-1]
    answer = INF
    for last_cut_gap_idx in range(num_gaps):
        tail_sum = sum_of_gaps(last_cut_gap_idx + 1, num_gaps - 1)
        total_max = max(dp[cut_num - 1][last_cut_gap_idx], tail_sum)
        if total_max < answer:
            answer = total_max
    return answer


if __name__ == "__main__":
    query_count = int(input())
    house = []

    for _ in range(query_count):
        command = list(map(int, input().split()))
        command_type = command[0]

        if command_type == 100:
            initial_count = command[1]
            house = command[2:2 + initial_count]
            house.sort()

        elif command_type == 200:
            new_house_position = command[1]
            insert_pos = bisect_left(house, new_house_position)
            house.insert(insert_pos, new_house_position)

        elif command_type == 300:
            removal_index = command[1]
            if 1 <= removal_index <= len(house):
                house.pop(removal_index - 1)

        else:
            ant_cnt = command[1]
            num_houses = len(house)
            if num_houses <= 1:
                print(0)
                continue

            gap_lengths = [house[i] - house[i - 1] for i in range(1, num_houses)]
            print(solve_minimax_by_cuts(gap_lengths, ant_cnt))