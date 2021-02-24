# Q. 음이 아닌 정수들로 이루어진 배열이 있다.
# 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# 사용할 수 있는 숫자가 담긴 배열 numbers,
# 타겟 넘버 target_number이 매개변수로 주어질 때 숫자를 적절히
# 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.

# 3
# +1 #+1  2
# -1  0
# +1 #+1  2
# -1  0
# 2      4     8
input_array = [1, 1, 1, 1, 1]
target_number = 3
count_number = 0


def get_plus_minus_sum(index, input_array, result_number):
    #print(index,"|",result_number)
    if len(input_array) <= index:
        if result_number == target_number:
            global count_number
            count_number += 1
        return
    get_plus_minus_sum(index + 1, input_array, result_number + input_array[index])
    get_plus_minus_sum(index + 1, input_array, result_number - input_array[index])


get_plus_minus_sum(0, input_array, 0)
print(count_number)
