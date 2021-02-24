# 선택해서 정렬.  : 가장 작은 1과 맨앞자리 를 교체  반복
input = [10, 4, 2]
def selection_sort(input):
    n = len(input)
    for loop1 in range(n - 1):
        min_index = loop1
        for loop2 in range(n-loop1):
            print(min_index + loop2, min_index , input)
            if input[min_index] > input[loop1 + loop2]:
                min_index = loop1 + loop2
        input[loop1], input[min_index] = input[min_index], input[loop1]
    return input
print(selection_sort(input))
