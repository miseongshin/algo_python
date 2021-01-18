input = "011110"
#input = "00001111"

def find_count_to_turn_out_to_all_zero_or_all_one(string):

    sum = 0
    goal_num = 0
    for num in string:
        sum += int(num)
    if sum > len(string)/2:
        goal_num = 1

    if goal_num == 1:
        return len(string) - sum
    else:
        return sum

print(find_count_to_turn_out_to_all_zero_or_all_one(input))