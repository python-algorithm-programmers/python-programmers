def dfs(cnt, vowel_cnt, consonant_cnt, L, words_dict, create, total):
    if cnt == L and vowel_cnt >= 1 and consonant_cnt >= 2:
        total.append(create)
        return

    # 글자를 못붙인 경우에도 멈춤
    if cnt == L:
        return

    # 선택을 해야됨
    for alphabet, packed in words_dict.items():
        order, visited = packed
        v_flag = False

        if not visited:
            # 모음인지, 자음인지 구분
            if alphabet in ["a","e","i","o","u"]:
                v_flag = True

            # 문자 생성 시작인 경우, 묻지않고 바로 글자로 붙임
            if create == "":
                create += alphabet
                words_dict[alphabet][1] = True
                if v_flag:
                    dfs(cnt+1, vowel_cnt+1, consonant_cnt, L, words_dict, create, total)
                else:
                    dfs(cnt+1, vowel_cnt, consonant_cnt+1, L, words_dict, create, total)

                # 참조변수, 레퍼런스라서 백트래킹 필요
                words_dict[alphabet][1] = False
                create = create[:-1]

            else:
                last_word = create[-1]
                last_word_order = words_dict[last_word][0]

                # 이전 단어의 순서만 비교하는 식을 반복해서
                # 생성되었던 단어들이 순서대로 나열되어있음을 고려
                if order > last_word_order:
                    create += alphabet
                    words_dict[alphabet][1] = True
                    if v_flag:
                        dfs(cnt + 1, vowel_cnt + 1, consonant_cnt, L, words_dict, create, total)
                    else:
                        dfs(cnt + 1, vowel_cnt, consonant_cnt + 1, L, words_dict, create, total)

                    # 참조변수, 레퍼런스라서 백트래킹 필요
                    words_dict[alphabet][1] = False
                    create = create[:-1]
def solution(L, words_dict):
    total = []
    dfs(0, 0,0, L, words_dict, "", total)
    for word in total:
        print(word)

if __name__ == "__main__":
    L, C = list(map(int, input().split(" ")))
    words = input().split(" ")
    words.sort()
    words_dict = {word: [int(ord(word) - 96), False] for word in words}
    solution(L, words_dict)