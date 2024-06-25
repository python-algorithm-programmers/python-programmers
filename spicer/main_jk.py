import heapq

def solution(scovilles, k):
    # heap 구조에서는 정렬이 아니라, 최솟값만 쉽게 담아낼 수 있다는 것을 참조해서
    # 정렬하는 것이 아닌 최솟값, 2번째 최솟값만 pop의 형태로 뽑아서 구현하는 것을 목표
    # 10만개까지 원소가 존재하므로, 새로 할당하는 것이 아닌 기존의 scovilles 리스트를 사용
    cnt = 0

    # scovilles 리스트를 heap 자료형으로 변환, 시간복잡도 O(n)
    heapq.heapify(scovilles)
    while True:
        # 종료 조건을 따로 만듦
        if scovilles[0] >= k:
            break

        elif len(scovilles) < 2:
            return -1

        else:
            min_val = heapq.heappop(scovilles)
            sec_min_val = heapq.heappop(scovilles)

            heapq.heappush(scovilles, min_val+sec_min_val*2)
            cnt += 1

    return cnt

if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 10, 12], 7))