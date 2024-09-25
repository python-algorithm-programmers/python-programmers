# def solution(s):
#     str_list = s.split(" ")
#     print(str_list)
#     answer = []
#     for word in str_list:
#         new_word = word[0].upper() + word[1:].lower()
#         answer.append(new_word)
#
#     return ' '.join(answer)

def solution(s):
    answer = ''
    char_flag = False
    for char in s:
        if char != ' ':
            if not char_flag:
                answer += char.upper()
                char_flag = True
                continue
            answer += char.lower()

        else:
            char_flag = False
            answer += char

    return answer

if __name__ == '__main__':
    print(solution("3people Unfollowed Me"))