# GCD
# GCD : Greatest common divisor : 최대공약수
# 유클리드 호제법
# : a,b에 대해 a를 로 나눈 나머지를 r이라 하면
#    a,b의 최대 공약수는  b와 r의 최대 공약수와 같다.
#   a   b
#  192  162
#  162  30
#  30   12
#  12   6   >> 최대 공약수 6


def gcd(a, b):
    print("---" + str(a) + ", " + str(b))
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(192, 162))
