input = "abacabade"


def find_not_repeating_character(string):
    alphabet_array = [0]*26
    for num in string:
        if not num.isalpha():
            continue
        alphabet_array[ord(num)-ord("a")] += 1

    for num in string:
        if alphabet_array[ord(num)-ord("a")] == 1:
            return num
    return "NONE"

def find_not_repeating_character2(string):
    alphabet_array = [0]*26
    for num in string:
        if not num.isalpha():
            continue
        alphabet_array[ord(num)-ord("a")] += 1
    not_repeating_character_array = []
    for index in range(len(alphabet_array)):
        alphabet_occurrence = alphabet_array[index]
        if alphabet_occurrence ==1:
            not_repeating_character_array.append(chr(index+ord("a")))
    return not_repeating_character_array
print(find_not_repeating_character(input))
print(find_not_repeating_character2(input))