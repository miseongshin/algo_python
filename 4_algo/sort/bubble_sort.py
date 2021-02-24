input = [10, 4,2]

def bubble_sort(input):
    n = len(input)
    for loop1 in range(n - 1):
        for loop2 in range(n - 1 - loop1):
            print(loop2, loop2 + 1, input)
            if input[loop2] > input[loop2 + 1]:
                input[loop2], input[loop2 + 1] = input[loop2 + 1], input[loop2]

    return input


print(bubble_sort(input))
