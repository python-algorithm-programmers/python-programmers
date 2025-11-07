"""
BFS로 이모티콘, 할인율의 조합을 모두 완전탐색

[완전 탐색]
- 할인율 -> 1~99로 이모티콘마다 적용
- 할인율을 다르게 적용했을 때, 총 비용과 서비스 가입자 수 적용

def dfs():
    if depth == N:
        total_spent[0] = spent
        total_subscribe[0] = subscribe
        return

    for dc in range(1, 100):
        user_dc, user_boundary = users[depth]
        for emtc in emoticons:
            if dc >= user_dc:
                add_spent += (emtc * (100 - dc)) // 100

        if spent >= user_boundary:
            dfs(subscribe+1, spent, depth+1)

        else:
            dfs(subsribe, spent+add_spent, depth+1)

"""


def solution(users, emoticons):
    N = len(emoticons)
    emoc_dc = []
    total_discount = []
    result = []

    def eval(users, total_discount):
        for combi in total_discount:
            total_spent = 0
            total_subscribe = 0
            for user_dc, user_boundary in users:
                user_spent = 0
                for emotion, discount in combi:
                    if discount >= user_dc:
                        user_spent += (emotion * (100-discount)) // 100

                if user_spent >= user_boundary:
                    total_subscribe += 1
                else:
                    total_spent += user_spent

            result.append([total_subscribe, total_spent])

    # 계산하는 파트는 따로 두기
    # 이모티콘과 할인율의 조합
    def dfs(depth):
        if depth == N:
            total_discount.append(emoc_dc[:])
            return

        emtc = emoticons[depth]
        for dc in [10, 20, 30, 40]:
            emoc_dc.append([emtc, dc])
            dfs(depth+1)
            emoc_dc.pop()
    dfs(0)
    eval(users, total_discount)
    result.sort(key=lambda x:([-x[0], -x[1]]))
    return result[0]


if __name__ == "__main__":
    users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
    emoticons = [1300, 1500, 1600, 4900]
    print(solution(users, emoticons))