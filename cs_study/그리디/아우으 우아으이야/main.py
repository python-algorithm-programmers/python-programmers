

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    lines = []
    total_line = 0
    N = int(input())
    for _ in range(N):
        min_p, max_p = map(int, input().split())
        if not lines:
            lines.append((min_p, max_p))
            total_line += max_p - min_p
            continue

        last_line = lines.pop()
        min_check, max_check = last_line
        total_line -= abs(max_check - min_check)

        # 내부 범위에 포함
        if min_check <= min_p and max_p <= max_check:
            lines.append(tuple(last_line))
            total_line += abs(max_check - min_check)

        # 작은 부분만 포함
        elif min_p <= min_check and min_check <= max_p <= max_check:
            lines.append((min_p, max_check))
            total_line += abs(max_check - min_p)

        # 큰 부분만 포함
        elif min_check <= min_p <= max_check and max_check <= max_p:
            lines.append((min_check, max_p))
            total_line += abs(max_p - min_check)

        # 없으면 추가하는 형태로
        else:
            lines.append(tuple(last_line))
            lines.append((min_p, max_p))
            total_line += abs(max_check - min_check)
            total_line += max_p - min_p

    #print(lines)
    print(total_line)