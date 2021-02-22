# 005 정수입력시 그이하 소수 출력
number = 100


# 소수 : 약수가 1과 자기자신밖에 없는것.
# N이 N의 제곱근보다 크지 않은 어떤소수로도 나눠지지 않는다.

def find_prime_list_under_number(number):
    prime_list = []
    count = 0
    for n in range(2, number + 1):
        for i in prime_list:
            count += 1
            if n % i == 0 and i * i <= n:
                break
        else:  # 브레이크가 한번도 실행안되었을때
            prime_list.append(n)
    print("최종:", count)
    return prime_list


def find_prime_list_under_number1(number):
    prime_list = []
    count = 0
    for n in range(2, number + 1):
        for i in range(2, n):
            count += 1
            if n % i == 0:
                break
        else:
            prime_list.append(n)
    print("1:", count)
    return prime_list


def find_prime_list_under_number2(number):
    prime_list = []
    count = 0
    for n in range(2, number + 1):
        for i in prime_list:  # 2~ n-1 중에서 소수인 친구들만
            count += 1
            if n % i == 0:
                break
        else:  # 브레이크가 한번도 실행안되었을때
            prime_list.append(n)
    print("2", count)
    return prime_list


print(find_prime_list_under_number1(number))

print(find_prime_list_under_number2(number))

print("최종: ", find_prime_list_under_number(number))
