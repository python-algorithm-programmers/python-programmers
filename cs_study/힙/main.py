

if __name__ == "__main__":
    N = int(input())
    results = []
    for _ in range(N):
        print_num = int(input())
        if print_num != 0:
            if not results:
                results.append(print_num)
                continue

            for i, num in enumerate(results):
                if abs(num) == abs(print_num) and num > print_num:
                    results.insert(i, print_num)
                    break
                elif abs(num) == abs(print_num) and num < print_num:
                    results.insert(i+1, print_num)
                    break
                elif abs(num) == abs(print_num) and num == print_num:
                    results.insert(i+1, print_num)
                    break

                # 입력받은 수의 절댓값이 더 작은 경우
                elif abs(num) > abs(print_num) and num > print_num:
                    results.insert(i, print_num)
                    break

                elif abs(num) > abs(print_num) and num < print_num:
                    results.insert(i, print_num)
                    break

                # 그냥 제일 크면 맨 뒤로 붙이기
                elif abs(results[-1]) < abs(print_num):
                    results.append(print_num)
                    break

                # 입력받은 수의 절댓값이 더 큰 경우, 다음 값으로 넘김
                else:
                    continue

        # 0인 경우
        else:
            if not results:
                print(0)
            else:
                print(results.pop(0))