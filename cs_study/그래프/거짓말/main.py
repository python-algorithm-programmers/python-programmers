
if __name__ == "__main__":
    N, M = map(int, input().split())
    true_input = list(map(int, input().split()))
    # 중복이 될 수 있으므로
    true_mans = set(true_input[1:])
    party_rounds = []
    for _ in range(M):
        line = list(map(int, input().split()))
        party_rounds.append(line[1:])

    is_true = True
    while is_true:
        is_true = False
        for party_mans in party_rounds:
            # 진실의 그룹에 속한 인물이 단 한사람이라도 존재하면
            if any(party_man in true_mans for party_man in party_mans):
                # 그 라운드에 속한 모든 인물은 진실의 그룹에 속함
                for man in party_mans:
                    if man not in true_mans:
                        true_mans.add(man)
                        # 계속 돌려면 true 값 바꿔줌
                        is_true = True

    # 다 바꿔주고 나서 파티 수 계산
    cnt = 0
    for party_man in party_rounds:
        if any(man in true_mans for man in party_man):
            continue
        else:
            cnt += 1

    print(cnt)
