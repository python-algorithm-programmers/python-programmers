def solution(cards1, cards2, goal):
    card1_idx = 0
    card2_idx = 0
    goal_idx = 0

    # goal 리스트에서 하나의 원소마다 제한을 적용해야함
    for goal_word in goal:


        if cards1[card1_idx] == goal_word:
            if card1_idx + 1 < len(cards1):
                card1_idx += 1
                continue

        elif cards2[card2_idx] == goal_word:
            if card2_idx + 1 < len(cards2):
                card2_idx += 1
                continue
        else:
            return "No"

    return "Yes"

if __name__ == '__main__':
    print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))