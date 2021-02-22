# 004 반복되지 않은 첫번째 문자출력
# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.
# "abadabac" # 반복되지 않는 문자는 d, c 가 있지만 "첫번째" 문자니까 d를 반환해주면 됩니다!
import re

#input = "abadabac"
input = "abab"

def find_not_repeating_first_character(input):
    ascii_a = ord("a")
    ascii_z = ord("z")
    occured_alphabet = [0] * (ascii_z - ascii_a + 1)
    # print(ord("z")-ord("a")+1)
    input_param = input.lower()
    input_param = re.sub("[^a-z]", "", input_param)
    for text in input_param:
        occured_alphabet[ord(text)-ascii_a] += 1
    #print("occured_alphabet: ",occured_alphabet)

    for text in input_param:
        if occured_alphabet[ord(text) - ascii_a] == 1:
            return text
    return "_"


print(find_not_repeating_first_character(input))

