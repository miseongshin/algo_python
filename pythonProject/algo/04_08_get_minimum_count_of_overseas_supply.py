import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

# 0일 4
# 1일 3
# 2일 2
# 3일 1
# 현재 재고가 바닥나는 시점 이전까지 받을 수 있는 라면중 제일 많은 라면을 받는게 목표
# 1. 현재 재고의 상태에 따라 최고값을 받아야 한다.
# 2. 제일 많은 값만 가져가면 된다.

# 1. 데이터를 넣을 때마다 최솟/최댓값을 동적ㅇ로 변경시키며
# 2. 최솟/최댓값을 꺼낼 수 있는 자료구조.



def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):

    anser = 0
    cur_day_idx = 0
    max_heap = []

    while stock < k:
        #date 를 기준으로 반복
        for date_idx  in range(cur_day_idx, len(dates)):
            if dates[date_idx] <= stock :  #10<4
                heapq.heappush(max_heap, -supplies[date_idx])
            else:
                cur_day_idx = date_idx
                break
        anser +=1
        stock += -heapq.heappop(max_heap)

    return anser


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))