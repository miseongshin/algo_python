# 회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 말합니다
# 토마토 오디오
# 한글자도 회문
def is_palindrome(string):

    string_len = len(string)
    if string_len <= 1:
        return True
    ##print(string[:1], "|", string[string_len - 1:])
    #if string[:1] != string[string_len - 1:]:
    if string[:1] != string[- 1]:
        return False
    else:
        return is_palindrome(string[1:- 1])


print(is_palindrome("abcba"))
print(is_palindrome("abcㅊㅊㅊba"))
