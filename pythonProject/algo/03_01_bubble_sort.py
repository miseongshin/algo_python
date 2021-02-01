input = [4, 6, 2, 9, 1]
# 총 비교는 4번 반복
# -> -> -> ->
#46291
# -> -> ->
#42619
# -> ->
#24169
# ->
#21469
#O(n^2)
def bubble_sort(array):
    n = len(array)
    for x in range(n-1):
        for y in range(n-x-1):
            if array[y] > array[y+1]:
                array[y], array[y+1] = array[y+1], array[y]
            #print(x, array)
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!