import re

print("char to ASCII", ord("a"))

print("is alphabet or not".isalpha())

text = "I'm Going To Live Every Minute Of It."
text_mod = re.sub("[^a-z]", "", text)
print("re.sub（정규 표현식, 대상 문자열 , 치환 문자）", text_mod)

print("최소값", min(1, 3))


# global 변수 .. 전역변수 이용
#            global count_number
#            count_number += 1

# 딕셔너리
a = {1: "hi"}
a[2]="hello"
print(a.get(1))
print(a)
del a[1]
print(a)