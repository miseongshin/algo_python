input = [4, 6, 2, 9, 1]
#O(N^2)
#시그마 N

def insertion_sort(array):
    n = len(array)
    for x in range(1, n):
        for y in range(x):
            # print(x-y)
            if array[x - y - 1] > array[x - y]:
                array[x - y - 1], array[x - y] = array[x - y], array[x - y - 1]
            else:
                break
    return array


insertion_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
