import re

print("char to ASCII", ord("a"))

print("is alphabet or not".isalpha())

text = "I'm Going To Live Every Minute Of It."
text_mod = re.sub("[^a-z]", "", text)
print("re.sub（정규 표현식, 대상 문자열 , 치환 문자）", text_mod)

print("최소값", min(1, 3))
