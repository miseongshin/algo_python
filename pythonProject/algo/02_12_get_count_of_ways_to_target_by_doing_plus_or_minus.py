# numbers = [1, 1, 1, 1, 1]
# numbers = [1, 2, 3, 4, 5]
numbers = [2, 3, 1]
# 11111 : 1개
# -1 1111  1-1111 11-111 111-11 1111-1 : 5개
# -1-1111  -11-111 -111-11 -1111-1 : 5*4개
# -1-1-111 -11-1-11 -11-11-1 : 5*4개
# -1-1-1-11 -11-1-1-1  : 5개
# -1-1-1-1-1   1개
# -12345
# target_number = 3
target_number = 0

# 2+3+1 =6    +++
# 2+3-1 =4    ++-
# 2-3+1 =0    +-+
# 2-3=1 =-2   +--
# -2+3+1=2    -++
# -2+3-1=0    -+-
# -2-3+1=-4   -++
# -2-3-1=-7   ---
# N 길이의 배열에서 더하거나 뺀 모든 경우의 수는
# N-1 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수
result = []
result_count = 0


def get_all_number_plus_or_minus(array, currunt_idx, currunt_sum, all_ways):
    if currunt_idx == len(numbers):
        all_ways.append(currunt_sum)
        return
    get_all_number_plus_or_minus(array, currunt_idx + 1, currunt_sum + numbers[currunt_idx], all_ways)
    get_all_number_plus_or_minus(array, currunt_idx + 1, currunt_sum - numbers[currunt_idx], all_ways)


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, currunt_idx, currunt_sum, all_ways):
    if currunt_idx == len(numbers):
        if currunt_sum == target_number:
            global result_count
            result_count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, currunt_idx + 1, currunt_sum + numbers[currunt_idx], all_ways)
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, currunt_idx + 1, currunt_sum - numbers[currunt_idx], all_ways)

#get_all_number_plus_or_minus(numbers, 0, 0, result)
#print(result)
get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, 0,0,result)
print(result_count)  # 5를 반환해야 합니다!
