# print(ord("a"))
# print(ord("a")-ord("a"))
# print(ord("b")-ord("a"))

input = "hello my name is 0_sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    string = string.replace(" ", "")
    string_to_array = list(string)
    for num in string_to_array:
        alphabet_occurrence_array[ord(num) - ord("a")] +=1
    return alphabet_occurrence_array


def find_max_occurred_alphabet2(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
    return alphabet_occurrence_array


print(find_max_occurred_alphabet(input))

print(find_max_occurred_alphabet2(input))
