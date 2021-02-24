# 삽입 정렬은 전체에서 하나씩 올바른 위치에 "삽입" 하는 방식입니다
input = [10, 4, 2,3,5,7,]
def insertion_sort(input):
    n = len(input)
    for loop1 in range(n - 1):
        for loop2 in range(loop1):
            #print(loop1, loop2)
            print(loop1-loop2-1 ,loop1-loop2)
            if input[loop1-loop2-1] <input[loop1-loop2]:
                input[loop1-loop2-1],input[loop1-loop2] =input[loop1-loop2],input[loop1-loop2-1]
            else:
                break
    return input
print(insertion_sort(input))

#0 1

#1 2
#0 1

#2 3
#1 2
#0 1

#3 4
#2 3
#1 2
#0 1