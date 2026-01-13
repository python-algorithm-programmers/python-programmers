def solution(N, heap_list):
    result = 0

    # 1. 최소 힙으로 0 이하 인것들은 모두 곱셈 처리
    heapq.heapify(heap_list)
    while heap_list:
        min_num = heapq.heappop(heap_list)
        if min_num <= 0:
            # 다음 원소도 있는 지 확인
            if heap_list:
                # 다음 원소보고 곱셈할 지, 덧셈할 지 결정
                next_num = heapq.heappop(heap_list)
                if next_num <= 0:
                    result += min_num * next_num
                else:
                    result += min_num
                    heapq.heappush(heap_list, next_num)
                    break

            # 다음 원소가 없으면 그냥 더하기
            else:
                result += min_num
                break
        else:
            heapq.heappush(heap_list, min_num)
            break

    #print(result)
    #print(heap_list)
    #print("next")
    # 2. 이제 꺼낸 원소가 0보다 큰 경우
    # 최대 힙으로 전환
    heap_list = [-num for num in heap_list]
    heapq.heapify(heap_list)
    while heap_list:
        max_num = heapq.heappop(heap_list)
        if max_num < -1:
            if heap_list:
                next_num = heapq.heappop(heap_list)
                if next_num < -1:
                    result += max_num * next_num
                elif next_num == -1:
                    result += -max_num + -next_num
            else:
                result += -max_num
        else:
            if heap_list:
                next_num = heapq.heappop(heap_list)
                result += -max_num + -next_num
                #print(max_num, next_num)
            else:
                result += -max_num

    return result



if __name__ == "__main__":
    import heapq
    heap_list = []
    N = int(input())
    for _ in range(N):
        heap_list.append(int(input()))
    print(solution(N, heap_list))