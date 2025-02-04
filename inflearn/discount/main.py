def solution(prices, discount):
    prices = sorted(prices, key=lambda x:x, reverse=True)
    discount = sorted(discount, reverse=True)

    result = 0
    # 차례로 맵핑하면 됨
    while prices and discount:
        price = prices.pop()
        coupon = discount.pop()
        result += price * ((100-coupon) / 100)

    result += prices[0]
    return result



if __name__ == "__main__":
    prices = [30000, 2000, 1500000]
    discount = [20, 40]
    print(solution(prices, discount))