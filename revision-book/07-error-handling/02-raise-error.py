def add(n1, n2):
    if (type(n1) is int and type(n2) is int):
        return n1 + n2
    return 'Oops you passes wrong data types'

print(add(1, 3))
print(add(1, '3'))


def multiply(n1, n2):
    if (type(n1) is int and type(n2) is int):
        return n1 * n2
    # raise TypeError('Oops you passes wrong data types')
    raise ValueError('Values cannot be multiplied')

print(multiply(4, 5))
# print(multiply(4, '5'))  # TypeError: Oops you passes wrong data types
# print(multiply(4, '5'))  # ValueError: Values cannot be multiplied


def add(n1, n2):
    return n1 + n2

print(add(2, '3'))