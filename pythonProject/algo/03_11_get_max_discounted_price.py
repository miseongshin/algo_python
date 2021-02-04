shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

#Q1 최대한 할일을 많이 받는다면 얼마를 내야하는가?
def get_max_discounted_price(prices, coupons):
    prices.sort()
    coupons.sort()
    coupons_len = len(coupons)
    sum_price=0
    for idx in range(len(prices)):
        if coupons_len - idx -1> -1:
            price = prices[idx]*(1 - coupons[coupons_len-idx-1]/100)
        else:
            price = prices[idx]
        sum_price +=price
    return int(sum_price)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.