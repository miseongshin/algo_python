from typing import List

input = 20


def find_prime_list_under_number(number):
    primeList: list[int] = []
    for num in range(2, number + 1):
        if isPrime(int(num)):
            primeList.append(num)
    return primeList


def isPrime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    for idx in range(3, number, 2):
        # print(number ,"|",idx)
        if number % idx == 0: return False
    return True


print(find_prime_list_under_number(input))
