if __name__ == "__main__":
    import time
    N = int(input())
    num_arr = [0]*(N+1)

    # 에라토스 체
    for i in range(1, N+1):
        for j in range(i, N+1, i):
            num_arr[j] += 1
    print(num_arr[N])