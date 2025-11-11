
if __name__ == "__main__":
    import sys
    import heapq
    input = sys.stdin.readline

    N = int(input())
    for _ in range(N):
        T = int(input())
        heap_min = []
        heap_max = []
        heap_dict = {}
        for _ in range(T):
            cmd, input_data = input().split()
            input_data = int(input_data)
            if cmd == "I":
                heapq.heappush(heap_min, input_data)
                heapq.heappush(heap_max, -input_data)
                heap_dict[input_data] = heap_dict.get(input_data, 0) + 1
            else:
                if input_data == -1:
                    #print("before min heap_dict", heap_dict, heap_min)
                    while heap_min and heap_dict.get(heap_min[0], 0) == 0:
                        heapq.heappop(heap_min)

                    if heap_min:
                        min_data = heapq.heappop(heap_min)
                        #print(heap_dict.get(min_data))
                        if heap_dict.get(min_data):
                            heap_dict[min_data] -= 1
                            if heap_dict[min_data] == 0:
                                del heap_dict[min_data]
                        #print("after min_data", min_data, heap_min, heap_dict)

                else:
                    #print("before max heap_dict", heap_dict, heap_max)
                    while heap_max and heap_dict.get(-heap_max[0], 0) == 0:
                        heapq.heappop(heap_max)

                    #print(heap_max)
                    if heap_max:
                        max_data = heapq.heappop(heap_max)
                        max_data = -max_data
                        #print(heap_dict.get(max_data))
                        if heap_dict.get(max_data):
                            heap_dict[max_data] -= 1
                            if heap_dict[max_data] == 0:
                                del heap_dict[max_data]

                        #print("after max_data", max_data, heap_max, heap_dict)

        # 다 처리하고 난 뒤
        if not heap_dict:
            print("EMPTY")
        else:
            answer = []
            # Max
            while True:
                max_heap = heapq.heappop(heap_max)
                max_heap = -max_heap
                if max_heap not in heap_dict:
                    continue
                else:
                    answer.append(max_heap)
                    break

            # Min
            while True:
                min_heap = heapq.heappop(heap_min)
                if min_heap not in heap_dict:
                    continue
                else:
                    answer.append(min_heap)
                    break

            print(*answer)



