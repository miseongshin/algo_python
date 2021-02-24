array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]
array = [5, 3, 2, 1, 6, 8, 7, 4]

def merge_sort(array):

    if len(array)<=1:
        return array

    mid = len(array)//2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    print(left_array, right_array)
    return merge(left_array, right_array)

def merge(array1, array2):
    array_c =[]

    index_a = 0
    index_b = 0

    for i in range(len(array1)+len(array2)):
        #print(len(array1)+len(array2),i )
        #print(index_a,index_b)
        if len(array1) <= index_a:
            array_c.append(array2[index_b])
            index_b += 1
        elif len(array2) <= index_b:
            array_c.append(array1[index_a])
            index_a += 1
        elif array1[index_a] >= array2[index_b]:
            array_c.append(array2[index_b])
            index_b += 1
        else:
            array_c.append(array1[index_a])
            index_a += 1
    return array_c


print(merge(array_a,array_b))

print(merge_sort(array))