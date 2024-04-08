def solution(dirs):
    # dx, dy는 되지 않음
    # DFS가 아니기 때문에 정확한 방향과 거리이동 계산이 필요
    moving = {'U':(0,1), 'D':(0,-1),'L':(-1,0),'R':(1,0)}

    # 현재 위치
    current_pos = (0,0)

    # 1. 현재 위치와 다음 위치를 세트로 묶어 기억
    history = set()

    # 다음 위치 계산 + 두 좌표 기억
    for move in dirs:
        y, x = current_pos[0], current_pos[1]
        ny = y + moving[move][0]
        nx = x + moving[move][1]

        if -5 <= ny <= 5 and -5 <= nx <= 5:
            next_pos = (ny, nx)

            # 경로를 정렬하여 중복 제거
            path = tuple(sorted([current_pos, next_pos]))

            # set니깐 제거됨
            history.add(path)
            current_pos = next_pos

    # 중복된 좌표 (좌우 순서만 바뀌) 좌표 제거 후, 거리 계산
    # 중복 제거된 리스트
    return len(history)

if __name__ == '__main__':
    print(solution("ULURRDLLU"))