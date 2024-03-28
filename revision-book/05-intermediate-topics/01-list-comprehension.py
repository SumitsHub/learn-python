
##* List Comprehension - List comprehension is a concise way to create lists in Python.
# It allows you to create a new list by applying an expression to each item in an existing iterable (such as a list, tuple, or range) and optionally filtering the items based on a condition.

# If you are creating new list using loop over another list, then list comprehension

## Syntax -
# new_list = [expression for item in iterable if condition]
#* expression: The expression to evaluate for each item in the iterable. This expression will be applied to each item to create the elements of the new list.
#* item: The variable representing each item in the iterable.
#* iterable: The existing iterable (e.g., list, tuple, range) from which to extract items.
#* if condition (optional): A condition that filters the items. Only items for which the condition evaluates to True will be included in the new list.


##* Examples - 

#* Creating a List of Squares:

# Using a traditional loop
squares = []
for i in range(1, 6):
    squares.append(i * i)

# Using list comprehension
squares = [i * i for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]


#* Filtering Odd Numbers:

# Using a traditional loop
odd_numbers = []
for i in range(1, 11):
    if i % 2 != 0:
        odd_numbers.append(i)

# Using list comprehension
odd_numbers = [i for i in range(1, 11) if i % 2 != 0]
print(odd_numbers)  # [1, 3, 5, 7, 9]

# even numbers
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10]


#* Creating a List of Tuples:
# Using a traditional loop
pairs = []
for x in range(3):
    for y in range(3):
        pairs.append((x, y))

# Using list comprehension
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

#* Converting Strings to Uppercase:
words = ['hello', 'world', 'python']

# Using list comprehension
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']


#* Generating nested list
nested_list = [[i for i in range(1, 4)] for _ in range(3)]
print(nested_list)  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


#* Flattening a List of Lists:
# Nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using list comprehension
flattened_list = [num for sublist in nested_list for num in sublist]
print(flattened_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]


#* List comprehension with if-else
lst = [2, 4, 5, 7, 9, 10, 13, 12]

odd_even_list = ['Odd' if i % 2 != 0 else 'Even' for i in lst]
print(odd_even_list)  # ['Even', 'Even', 'Odd', 'Odd', 'Odd', 'Even', 'Odd', 'Even']
