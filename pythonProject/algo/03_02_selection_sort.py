input = [4, 6, 2, 9, 1]

# O(n^2)
def selection_sort(array):
    n = len(array)
    for x in range(n -1):
        min_index = x
        for y in range(n - x):
            if array[x+y]< array[min_index]:
                min_index = x + y
        array[x], array[min_index] = array[min_index], array[x]
    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!