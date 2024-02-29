def solution(cacheSize, cities):
    # 캐시를 저장할 리스트 or set
    cache_list = []
    answer = 0

    for city in cities:
        # cache_list 안에 새로 들어올 게 있는 지 확인, 없으면 5점
        if city.lower() not in cache_list:
            answer += 5

            if cache_list and len(cache_list) >= cacheSize:
                cache_list.pop(0)
                cache_list.append(city.lower())


            elif len(cache_list) < cacheSize:
                cache_list.append(city.lower())

        # 새로 들어올 게 있다면, 새로 들어온 것을 제거해주기
        else:
            answer += 1

            if cache_list and len(cache_list) >= cacheSize:
                cache_list.remove(city.lower())
                cache_list.append(city.lower())

            elif len(cache_list) < cacheSize:
                cache_list.remove(city.lower())
                cache_list.append(city.lower())

    return answer

if __name__ == '__main__':
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Seoul", "Pangyo", "Seoul", "NewYork", "Seoul"]))