
def solution(priorities, location):
    # queue를 생성할 튜플 리스트 생성
    queue = [(i,p) for i,p in enumerate(priorities)]

    # 맨처음 큐를 보고 다른 큐들과 비교하되, 작으면 뒤로 다시 넣고 제일 크다면 뽑기
    # 이때, 전체 순서 리스트를 만들지 않고 location까지만 확인하면 되므로
    # 해당 인덱스 일때, return

    answer_idx = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < other[1] for other in queue):
            queue.append(cur)

        else:
            answer_idx += 1
            if cur[0] == location:
                return answer_idx

if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))