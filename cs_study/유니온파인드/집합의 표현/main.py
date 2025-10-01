def find(i):
    if parents[i] != i:
        return find(parents[i])
    return i

def union(a, b):
    x = find(a)
    y = find(b)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


if __name__ == "__main__":
    n, m = map(int, input().split())
    parents = [0] * (n+1)
    for i in range(n+1):
        parents[i] = i

    for _ in range(m):
        cmd, s, k = map(int, input().split())
        if cmd == 0:
            union(s, k)

        elif cmd == 1:
            x = find(s)
            y = find(k)
            if x != y:
                print("NO")
            else:
                print("YES")



