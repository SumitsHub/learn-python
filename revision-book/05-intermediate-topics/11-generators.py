##* Generators

# * Revision - iterator v iterable

l = [1, 2, 3, 4]  # iterable
for num in l:
    print(num)

# Output:
# 1
# 2
# 3
# 4

# converting iterable to iterator using iter()
iterator = iter(l)
print(next(iterator))  # 1

# map iterator object
m_iter = map(lambda x: x**2, l)
print(type(m_iter))  # <class 'map'>

# NOTE: we can apply loop on both iterable and iterator
for num in m_iter:
    print(num)

# Output:
# 1
# 4
# 9
# 16

# print(next(m_iter))  # Error: StopIteration -> default value is not provided
print(
    next(m_iter, None)
)  # None -> defaultValue as iterator is exhausted by for loop above

# * Creating generators -
# Generators are iterators, memory efficient

# * 01: using generator function


def nums(n):
    for i in range(1, n + 1):
        yield i  # * yield keyword is used in generator instead of return


print(type(nums))  # <class 'function'>
print(nums(10))  # <generator object nums at 0x0000024D5C9F10E0>
print(type(nums(10)))  # <class 'generator'>

# for loop with generator
for num in nums(5):
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5

nums_iter = nums(5)
print(next(nums_iter))  # 1

for n in nums_iter:
    print(n)

# 2, 3, 4, 5


# * Generator comprehension

squares = (i**2 for i in range(1, 5))
# NOTE: using parenthesis for generator comprehension - there is no tuple comprehension it seems

for s in squares:
    print(s)
# 1
# 4
# 9
# 16

for s in squares:
    print(s)
# No Output - generator already exhausted by previous loop

squares = (i**2 for i in range(1, 5))
print(next(squares))  # 1

for s in squares:
    print(f"{int(s**0.5)}^2 = {s}")
# Output:
# 2^2 = 4
# 3^2 = 9
# 4^2 = 16
