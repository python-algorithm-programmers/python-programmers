from collections import deque

# 해야될 사항
# 1. 각 장르의 재생 횟수 구현, 각 장르 내의 재생 횟수 합계
# 2. 장르 내에서 가장 재생된 2곡 구하기, 각 장르 내에서 내림차순 정렬, 최대 2곡
# 3. 각 장르를 전체 재생 횟수 합에 따라 내림차순 정렬
# 4. 장르 내에서 노래 정렬할 때, play가 같으면 고유번호가 작은 순서대로 정렬

# 2가지 주요 포인트
# dictionary를 2개를 둠
# dictionary 저장시, 키값이 같을 때는 리스트로 해서 값을 넣는 생각
def solution(genres, plays):
    # 1. 장르별 총 재생 횟수 계산 및 장르별 노래 정보 저장
    # 장르별 총 재생횟수 dict, 장르와 (idx, play)로 묶은 dict 저장
    genre_total = {}
    genre_songs = {}

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_total[genre] = genre_total.get(genre, 0) + play

        if not genre_songs.get(genre):
            genre_songs[genre] = []

        genre_songs[genre].append((idx, play))

    # 장르를 순서 나열 리스트
    sorted_genre = sorted(genre_total.items(), key=lambda x:x[1], reverse=True)

    # 장르 내 플레이 리스트 나열
    result = []
    for genre, __ in sorted_genre:
        genre_songs[genre].sort(key=lambda x:(-x[1],x[0]))
        # genre 내에서 2개만 뽑기
        for song_idx, play in genre_songs[genre][:2]:
            result.append(song_idx)

    return result

if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))
