
##* iterator and iterables
# iterable
numbers = list(range(1, 4))  # list, string, tuple are iterables 

for num in numbers:
    print(num)

# iterator
squares = map(lambda x : x ** 2, numbers)
for num in squares:
    print(num)


##* iter() - converting iterable to iterator using iter()

numbers_iterator = iter(numbers)
print(numbers_iterator)  # list_iterator object
print(type(numbers_iterator))  # <class 'list_iterator'>

#* next() - Return the next item from the iterator. If default is given and the iterator is exhausted, it is returned instead of raising StopIteration.
print(next(numbers_iterator))  # 1
print(next(numbers_iterator))  # 2
print(next(numbers_iterator))  # 3 -> iterator exausted here
# print(next(numbers_iterator))  #* StopIteration

# looping through iterator, since iterator exausted above this loop don't do anything -> doesn't return ERROR also
for num in numbers_iterator:
    print(num)


#* using next() with built-in iterator
filter_iterator = filter(lambda x : x % 2 == 0, range(10))
print(filter_iterator)  # filter object
print(type(filter_iterator))  # <class 'filter'>
print(next(filter_iterator))  # 0
print(next(filter_iterator))  # 2
print(next(filter_iterator))  # 4


#* NOTE: 'range' object is not an iterator it's an iterable
# print(next(range(4)))  # ERROR: TypeError: 'range' object is not an iterator

# TODO: create other iterator for othet iterables (tuple, string)