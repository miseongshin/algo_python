# 002 최빈값 찾기, 최빈값==가장많은 빈도
import re

input = "I'm Going To Live Every Minute Of It."


# 정규 표현식(正規表現式, 영어: regular expression, 간단히 regexp[1] 또는 regex, rational expression)

def find_max_occured_alphabet(input):
    ascii_a = ord("a")
    ascii_z = ord("z")
    occured_alphabet = [0] * (ascii_z - ascii_a + 1)
    # print(ord("z")-ord("a")+1)
    input_param = input.lower()
    input_param = re.sub("[^a-z]", "", input_param)
    for text in input_param:
        occured_alphabet[ord(text)-ascii_a] += 1

    #print("occured_alphabet: ",occured_alphabet)

    max_occured_idx = 0
    max_occured_idx_value = occured_alphabet[0]
    for idx in range(len(occured_alphabet)):
        if max_occured_idx_value < occured_alphabet[idx]:
            max_occured_idx_value = occured_alphabet[idx]
            max_occured_idx = idx

    return chr(max_occured_idx + ascii_a)


print(find_max_occured_alphabet(input))
