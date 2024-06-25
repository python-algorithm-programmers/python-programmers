# 도달하기전 확인 -> 움직이는 메서드
# 최소 이동거리는 DFS는 매우 비효율적
# BFS로 접근하는 방법 효율적이다
def move(maps, position, size, count, visited, min_count):
    # move 호출하는 순간엔 이미 해당 위치에 방문했다고 가정한 것
    # 원래 위치 간단히 표현
    y, x = position

    # 한번 방문한 곳을 또 왔다는 건 이미 최단 루트 실패이므로 바로 -1 반환
    # 애초에 float('inf')로 값을 넣었놨고, min_count 값 변동이 없다면
    # 그대로 유지될 것이기에 아래의 코드를 그대로 냅둡
    # if visited[y][x]:
    #     return float('inf') # 이미 방문한 위치라면, 무한대 값을 반환

    # 2. 목표에 도달했는 지 확인 (종료 조건)
    if y == size[0] and x == size[1]:
        min_count[0] = min(min_count[0], count)
        return

    # 사전 확인 이후, 방문하지 않고 목표지점도 아니라면 방문처리
    visited[y][x] = True

    # 방향 벡터 선정 (동 -> 남 -> 서 -> 북) 순으로
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 1. 넘어갈 위치인 지 아닌 지 확인
    for i in range(len(dx)):
        ny, nx = y + dy[i], x + dx[i]

        # 최대 사이즈 안에 있는 지 확인 -> 넘어갈 위치가 1인지 확인
        if 0 <= ny <= size[0] and 0 <= nx <= size[1]:
            # 일부러 방문하지 않은 곳만 선택하지 않도록 함
            # 모든 루트가 -1을 반환하면 -1로 min_count를 반환하기 위함
            if maps[ny][nx] == 1:
                move(maps, (ny, nx), size, count + 1, visited, min_count)

    # 내부 재귀함수 함수 호출 후 다시, 외부 메서드에서 실행해야하므로 방문 처리 초기화
    # 백트래킹 (시도해보고 되돌아가기를 반복할 수 있도록)
    # 그러나 시도해보고 되돌아가기를 할 필요가 없이, 그냥 해당 루트는 -1 선언해도됨
    # 확실한 최단 거리만 찾으면 되기 때문
    # visited[y][x] = False

def solution(maps):
    # 위치를 기억할 변수 추가
    position = [0,0]

    # size 값 튜플로 설정, 어짜피 값은 바뀌지 않으므로 고정을 위해
    size = (len(maps) - 1, len(maps[0]) - 1)

    # False로 가득찬 2차원 배열 만들기
    visited = [[False] * (size[1] + 1) for _ in range(size[0] + 1)]
    min_count = [float('inf')]
    move(maps, position, size, 1, visited, min_count)
    return min_count[0] if min_count[0] != float('inf') else -1

if __name__ == '__main__':
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))