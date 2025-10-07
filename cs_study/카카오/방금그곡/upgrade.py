def tokenize_melody(music_str):
    """
    문자열을 '#' 음표 단위로 묶어서 리스트로 반환
    예: 'C#DEFGAB' -> ['C#', 'D', 'E', 'F', 'G', 'A', 'B']
    """
    notes = []
    for ch in music_str:
        if ch == '#':
            notes[-1] += '#'
        else:
            notes.append(ch)
    return notes


def build_played_melody(music, play_time):
    """
    음악 문자열과 재생 시간을 받아 실제 재생된 음표 리스트를 반환
    - 원래 곡 길이보다 짧으면 자르고
    - 길면 반복해서 채움
    """
    music_notes = tokenize_melody(music)
    length = len(music_notes)
    full_play = music_notes * (play_time // length) + music_notes[:(play_time % length)]
    return full_play


def contains_melody(full_play, target):
    """
    target 멜로디(m_list)가 full_play 안에 '연속적으로' 포함되어 있는지 검사
    """
    n, m = len(full_play), len(target)
    for i in range(n - m + 1):
        if full_play[i:i + m] == target:
            return True
    return False


def cal_time(start, end):
    """
    시작 시각과 끝 시각을 받아 총 재생 시간을 분 단위로 계산
    """
    start_h, start_m = map(int, start.split(':'))
    end_h, end_m = map(int, end.split(':'))
    return (end_h * 60 + end_m) - (start_h * 60 + start_m)


def solution(m, musicinfos):
    target = tokenize_melody(m)  # 찾을 멜로디
    candidates = []

    for idx, info in enumerate(musicinfos):
        start, end, title, music = info.split(',')
        play_time = cal_time(start, end)
        full_play = build_played_melody(music, play_time)

        # target이 full_play 안에 포함되어 있다면 후보로 추가
        if contains_melody(full_play, target):
            candidates.append((title, play_time, idx))

    # 일치하는 곡이 없는 경우
    if not candidates:
        return "(None)"

    # 재생 시간 내림차순, 먼저 입력된 순서(idx 오름차순)
    candidates.sort(key=lambda x: (-x[1], x[2]))
    return candidates[0][0]


# ✅ 테스트
if __name__ == "__main__":
    m = "ABC"
    musicinfos = [
        "12:00,12:14,HELLO,C#DEFGAB",
        "13:00,13:05,WORLD,ABCDEF"
    ]
    print(solution(m, musicinfos))  # ✅ 기대 결과: WORLD