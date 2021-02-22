s = "(())()"
#s = ")("

def is_correct_parenthesis(string):
    resultNum=0
    for str in string:
        if "(" == str:
            resultNum +=1
        elif ")" == str:
            resultNum -=1

        if resultNum < 0:
            break

    if resultNum == 0 : return True
    else: return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!