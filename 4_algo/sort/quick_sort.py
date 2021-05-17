input = [10, 4, 2]
def quick_sort(input):
    data_length = len(input)
    if data_length <=1:
        return input
    pivot = input[data_length//2]
    min = []
    max = []
    for num in range(data_length):
        if input[num] < pivot:
            min.append(input[num])
        elif input[num] > pivot:
            max.append(input[num])
    return quick_sort(min)+[pivot]+ quick_sort(max)
print(quick_sort(input))
