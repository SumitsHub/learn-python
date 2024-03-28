## tuple have less built-in methods than list since tuples are immutable

##* count(): Returns the number of occurrences of a specified value in the tuple.

my_tuple = (1, 2, 3, 2, 4, 2, 5)

# Count occurrences of value 2
count = my_tuple.count(2)
print("Count of 2:", count)  # Output: Count of 2: 3


##* index(): Returns the index of the first occurrence of a specified value in the tuple.

my_tuple = ('a', 'b', 'c', 'b')

# Find the index of 'b'
index = my_tuple.index('b')
print("Index of 'b':", index)  # Output: Index of 'b': 1
