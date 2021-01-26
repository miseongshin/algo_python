finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


# 정렬 되어 있지 않으면 이진탐색 불가

def is_exist_target_number_linner(target, numbers):
    for idx in range(len(finding_numbers)):
        if finding_numbers[idx] == finding_target:
            return True
    return False


result = is_exist_target_number_linner(finding_target, finding_numbers)
print(result)
