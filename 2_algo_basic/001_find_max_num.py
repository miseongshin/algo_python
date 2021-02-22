# 001 최대값을 찾아라

input = [1, 10, 4, 6, 7, 8, 9]


def find_max_num(input):
    max_num = input[0]
    for idx in range(1,len(input)):
        if max_num < input[idx]:
            max_num = input[idx]
    return max_num

print(find_max_num(input))
