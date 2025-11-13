from collections import deque


def solution(s):
    total = []
    max_size = len(s) // 2 + 1
    for size in range(1, max_size):
        string = s
        result = deque()

        # 문자 잘라서 stack으로 설정
        while len(string) > 0:
            if size <= len(string):
                new_s = string[:size]
                string = string[size:]
                result.append(new_s)
            else:
                result.append(string)
                string = ""

        # 자른 거 모아서 문자열 만들고 total 리스트에 저장
        past = None
        stack_cnt = 1
        result_str = ""
        # print(result)
        while result:
            cur = result[0]
            if len(result) > 1:
                if past == cur:
                    stack_cnt += 1
                    result.popleft()
                    continue

                else:
                    if past:
                        if stack_cnt > 1:
                            result_str += f"{stack_cnt}{past}"
                        else:
                            result_str += f"{past}"

                        stack_cnt = 1
                    past = cur
                    result.popleft()
            else:
                if past == cur:
                    stack_cnt += 1
                    result_str += f"{stack_cnt}{past}"
                    result.popleft()

                else:
                    if past:
                        if stack_cnt > 1:
                            result_str += f"{stack_cnt}{past}"
                        else:
                            result_str += f"{past}"

                    result_str += f"{cur}"
                    result.popleft()

        # print(result_str)
        total.append(len(result_str))

    total.sort()
    return total[0]