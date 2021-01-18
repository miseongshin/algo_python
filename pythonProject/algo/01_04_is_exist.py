input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    result = False
    for num in array:
        if num == number:
            result = True
    return result

def is_number_exist2(number, array):
    for num in array:
        if num == number:
            return  True
    return False
print(is_number_exist(3, input))
print(is_number_exist2(3, input))
#운이 좋으면 1  운이 나쁘면 N