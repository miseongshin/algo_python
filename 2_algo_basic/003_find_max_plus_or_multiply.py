# 003 곱하기 or 더하기 선택 가장큰수는?
# Q. 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 '✕' 혹은 '+' 연산자를 넣어 결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오.
# 단, '+' 보다 '✕' 를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서 순서대로 이루어진다.
input = [0, 3, 5, 6, 1, 2, 4]


# 1이하는 더하고 크면 곱한다.

def find_max_plus_or_multiply(input):
    result = input[0]

    for idx in range(1, len(input)):
        if input[idx] >= 1:
            result += input[idx]
        else:
            result *= input[idx]

    return result


print(find_max_plus_or_multiply(input))
