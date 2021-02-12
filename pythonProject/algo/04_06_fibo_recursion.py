input = 100

#fibo3   1,2 연산량 1 + 1 번
#fibo4   23        3 + 2 번
#fibo5  fibo4  fibo3
       #fibo4 ->    같은것을 계속 계산... 반복하지 않도록 동적계획법 사용.


def fibo_recursion(n):
    if n == 1 or  n == 2:
        return 1
    else:
        print(n)
        return fibo_recursion(n-2) + fibo_recursion(n-1)


print(fibo_recursion(input))  # 6765