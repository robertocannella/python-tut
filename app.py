# arguments

def multiply(a, b):
    return a*b


multiply(1, 3)


def multiplyAlt(*list):
    total = 1
    for number in list:
        total *= number
    return total
    print(list)


print(multiplyAlt(1, 2, 3, 4))
