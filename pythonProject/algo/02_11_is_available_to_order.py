shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# 현재 주문가능한 상태인지 여부를 반환

def is_available_to_order(menus, orders):
    order_cnt = len(orders)
    order_len = order_cnt
    
    for idx in range(len(orders)):

        if order_cnt + idx != order_len: return False
        for idx2 in range(len(menus)):
            if orders[idx] == shop_menus[idx2]:
                order_cnt -= 1
                break

    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
