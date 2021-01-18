input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    maxnum = 0;
    for num in array:
        if num > maxnum:
            maxnum = num
    return maxnum


def find_max_num2(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


def find_max_num3(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num

result = find_max_num(input)
print("find_max_num1", result)

result2 = find_max_num2(input)
print("find_max_num2", result2)

result3 = find_max_num3(input)
print("find_max_num3", result3)
