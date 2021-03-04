shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


# 퀵정렬이 가장 빠름. 파이썬.sort()


def get_max_discounted_price(prices, coupons):
    prices.sort()
    coupons.sort()
    print(coupons, prices)

    price_sum = 0
    while len(shop_prices) > 0:
        price = shop_prices.pop()
        #print(price)
        if len(coupons) == 0:
            price_sum += price
        else:
            #print(coupons.pop())
            price_sum += price * (100 - coupons.pop())//100
    return price_sum


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
