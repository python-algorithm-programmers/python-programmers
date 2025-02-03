top_heights = [6, 9, 5, 7, 4]

def get_receiver_top_orders(heights):
    answer = [0] * len(heights)

    while heights:
        height = heights.pop()
        for i in range(len(heights)-1, -1, -1):
            if height < heights[i]:
                answer[len(heights)] = i+1
                break
    return answer

print(get_receiver_top_orders(top_heights))


