seat_count = 9
vip_seat_array = [4, 7]


# [1,2,3,4,5,6,7,8,9,]
# 죄석 [1,2]
# [1,2] [2,3]
# 좌석 [1,2,3]
# [1,2,3] [2,1,3], [1,3,2]
# 좌석 [1,2,3,4]
# [1,2,3,4][1,2,4,3][1,3,2,4][2,1,3,4][2,1,4,3]
#F(2) = 2
#F(3) = 3
#F(4) = 5
#..피보나치

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    cur_index = 0
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat -1

        count_of_ways = fibo_dynamic_programming(fixed_seat_index - cur_index, memo)
        all_ways += count_of_ways
        cur_index = fixed_seat_index +1

    count_of_ways = fibo_dynamic_programming(total_count -cur_index,memo)
    all_ways *= count_of_ways
    return all_ways

memo = {
    1: 1,
    2: 2
}
def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo)+ fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    # print(nth_fibo)
    return nth_fibo
# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
