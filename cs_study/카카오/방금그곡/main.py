def listify_melody(music_str):
    notes = []
    for ch in music_str:
        if ch == "#":
            notes[-1] += "#"
        else:
            notes.append(ch)

    return notes

def build_melody(music, play_time):
    # 음악 문자열과 재생시간 받아서 실제 재생된 음표 리스트 반환
    music_notes = listify_melody(music)
    length = len(music_notes)
    full_play = music_notes * (play_time // length) + music_notes[:(play_time % length)]
    return full_play

def contains_melody(full_play, target):
    # 슬라이딩 윈도우로 리스트끼리 비교
    # 리스트끼리 비교는 set 처럼 포함관계로 할 수 없기에 슬라이딩 윈도우로 적용함
    n, m = len(full_play), len(target)
    for i in range(n - m + 1):
        if full_play[i:i+m] == target:
            return True
    return False


def cal_time(start, end):
    start_h, start_m = map(int, start.split(":"))
    end_h, end_m = map(int, end.split(":"))
    return (end_h*60 + end_m) - (start_h*60 + start_m)



def solution(m, musicinfos):
    # 멜로디 리스트 반환
    target = listify_melody(m)
    answer = []

    for idx, info in enumerate(musicinfos):
        start, end, title, music = info.split(',')
        play_time = cal_time(start, end)
        full_play = build_melody(music, play_time)

        # m_list가 full_play 안에 포함되어있으면 답으로 일단 포함해둠
        #print(full_play, target)
        if contains_melody(full_play, target):
            answer.append((title, play_time, idx))

    if not answer:
        return "(None)"

    answer.sort(key=lambda x: (-x[1], x[2]))
    return answer[0][0]




if __name__ == "__main__":
    m = "ABC"
    musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    print(solution(m, musicinfos))
