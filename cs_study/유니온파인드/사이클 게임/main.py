import sys


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    x = find(a)
    y = find(b)

    # 만약 서로 부모가 같다면, 한바퀴를 도는
    # 필요없는 추가 간선이므로 사이클이 됨
    if x == y:
        return True

    elif x < y:
        parents[y] = x

    else:
        parents[x] = y

    return False


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    parents = [0] * n
    flag = False
    for i in range(n):
        parents[i] = i

    for i in range(1, m+1):
        input_a, input_b = map(int, input().split())
        if union(input_a, input_b):
            print(i)
            flag = True
            break

    if not flag:
        print(0)
