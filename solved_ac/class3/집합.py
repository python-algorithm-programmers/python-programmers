def _add(S, x):
    S.add(x)

def _remove(S, x):
    S.discard(x)

def _check(S, x):
    return 1 if x in S else 0

def _toggle(S, x):
    if x in S:
        S.remove(x)
    else:
        S.add(x)

def _all(S, x):
    S.clear()
    S.update(range(1,21))

def _empty(S, x):
    S.clear()

_ops = {
    "add": _add,
    "remove": _remove,
    "check": _check,
    "toggle": _toggle,
    "all": _all,
    "empty": _empty,
}
def solution(method_name, check_list, num=None):
    result = _ops[method_name](check_list, num)
    if method_name == "check":
        return result

if __name__ == "__main__":
    M = int(input())
    check_list = set()
    for _ in range(M):
        method_list = input().split()
        if len(method_list) == 2:
            method_name, number = method_list
            ans = solution(method_name, check_list, int(number))
        else:
            method_name = method_list[0]
            ans = solution(method_name, check_list)
        if ans is not None:
            print(ans)