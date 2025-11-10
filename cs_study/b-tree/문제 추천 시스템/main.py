
if __name__ == "__main__":
    import sys
    import heapq
    input = sys.stdin.readline
    N = int(input())
    heap_min = []
    heap_max = []
    p_l_dict = {}
    for _ in range(N):
        P, L = map(int, input().split())
        heapq.heappush(heap_min,(L, P))
        heapq.heappush(heap_max,(-L, -P))
        p_l_dict[P] = L

    M = int(input())
    #print(p_l_dict)
    for _ in range(M):
        command = input().split()
        if command[0] == "add":
            P = int(command[1])
            L = int(command[2])
            heapq.heappush(heap_min, (L, P))
            heapq.heappush(heap_max, (-L, -P))
            p_l_dict[P] = L

        elif command[0] == "recommend":
            check_num = int(command[1])
            #print(remove_set)
            #print(heap_min)
            #print(heap_max)
            if check_num == -1:
                while True:
                    l, p = heap_min[0]
                    if p not in p_l_dict or p_l_dict[p] != l:
                        #print(heap_min)
                        heapq.heappop(heap_min)
                        continue
                    else:
                        #print(heap_min)
                        print(p)
                        #print()
                        break

            else:
                while True:
                    #print(heap_max)
                    minus_l, minus_p = heap_max[0]
                    p = minus_p * -1
                    l = minus_l * -1
                    if p not in p_l_dict or p_l_dict[p] != l:
                        heapq.heappop(heap_max)
                        continue
                    else:
                        print(-heap_max[0][1])
                        break

        elif command[0] == "solved":
            p_num = int(command[1])
            if p_num in p_l_dict:
                del p_l_dict[p_num]



