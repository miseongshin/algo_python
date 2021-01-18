input = [0, 3, 5, 6, 1, 2, 4]

# 1 이하는 더하는게 낫고  1초과는 곱하는게 낫다
# 결과  , 입력 수 동일하게 적용

def find_max_plus_or_multiply(array):
    result =0;
    for idx in range(len(array)):
        if result <= 1 or array[idx] <= 1:
            result += array[idx]
        else:
            result *=array[idx]
    return result

print(find_max_plus_or_multiply(input))