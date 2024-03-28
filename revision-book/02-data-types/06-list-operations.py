l1 = [1, 2, 3, 'Four']
l2 = [1, 2, 3, 'Four']

##* Adding 2 lists using +
res = l1 + l2
print(res)

##* Subtraction, Multiplication and Division with list - NOT ALLOWED
# print(l1 - l2)  # TypeError
# print(l1 * l2)  # TypeError
# print(l1 / l2)  # TypeError


##* min & max method with list
nums = [1, 2, 3, 10, 1000, -20, 20, 0]
alphas = ['a', 'b', 'c', 'dog', 'zebra', 'Apple', 'Ball']
alphanums = [1, 'a', 5, 25, 'cat']

print(min(nums))  # -20
print(min(alphas))  # Apple
print(min(['a', 'A']))  # A
# print(min(alphanums))  # TypeError: '<' not supported between instances of 'str' and 'int'

print(max(nums))  # 1000
print(max(alphas))  # zebra
print(max(['a', 'A']))  # a
# print(max(alphanums))  # TypeError: '>' not supported between instances of 'str' and 'int'


##* sorted() method with list - Returns a new list containing all items from the iterable in ascending order.
# use reverse=true for descending order

# NOTE: list.sort() method mutates the list in place whereas sorted() method returns new (sorted) list

print(sorted(nums))  # [-20, 0, 1, 2, 3, 10, 20, 1000]
print(sorted(nums, reverse=True))  # [1000, 20, 10, 3, 2, 1, 0, -20]
print(sorted(alphas)) # ['Apple', 'Ball', 'a', 'b', 'c', 'dog', 'zebra']
print(sorted(alphas, reverse=True))  # ['zebra', 'dog', 'c', 'b', 'a', 'Ball', 'Apple']
# print(sorted(alphanums))  # TypeError: '<' not supported between instances of 'str' and 'int'