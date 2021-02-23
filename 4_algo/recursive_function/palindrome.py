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