array = [5, 3, 2, 1, 6, 8, 7, 4]

#O(N)  array길이  + array 2길이
#Merge_sort
#N/2^k=1   -> k=log2N
#K 단계만큼 반복하는데 각각 단계는 O(N) 만큼 시간복잡도
#즉, log2N*O(N) -> O(nlogN)
# [5, 3]         길이 N
# left:  [5]
# right:  [3]
# [2, 1]
# left:  [2]
# right:  [1]
 # [5, 3, 2, 1]
# left:  [3, 5]
# right:  [1, 2]
# [6, 8]
# left:  [6]
# right:  [8]
# [7, 4]
# left:  [7]
# right:  [4]
 # [6, 8, 7, 4]  길이 N/4 4개  = N
# left:  [6, 8]
# right:  [4, 7]
  # [5, 3, 2, 1, 6, 8, 7, 4]
# left:  [1, 2, 3, 5]
# right:  [4, 6, 7, 8]
  # [1, 2, 3, 4, 5, 6, 7, 8]

def merge_sort(array):

    if len(array) <= 1:
        return array

    mid = (0 + len(array))//2
    left_array = merge_sort(array[:mid])  #왼쪽 부분정렬
    right_array = merge_sort(array[mid:]) # 오른쪾 부분 정렬
    print(array)
    print("left: ",left_array)
    print("right: ",right_array)
    return merge(left_array, right_array)


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!