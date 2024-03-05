def fatigue(present, dungeons, count):
    # 마지막 재귀함수에서 값을 반환하기 위해 적용
    max_total_count = count

    for i, dungeon in enumerate(dungeons):
        if present >= dungeon[0]:
            # 다음 던전 탐험
            next_dungeons = dungeons[:i] + dungeons[i + 1:]

            # 최대 방문 수 업데이트
            temp_total_count = fatigue(present - dungeon[1], next_dungeons, count + 1)
            max_total_count = max(count, temp_total_count)

    # 탐험이 끝나서 탐험한 던전 수 반환
    return max_total_count

def solution(k, dungeons):
    count = 0
    count = fatigue(k, dungeons, count)
    return count

if __name__ == '__main__':
    print(solution(80, [[80,20],[50,40],[30,10]]))