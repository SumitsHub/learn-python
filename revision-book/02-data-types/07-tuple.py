## Tuple data structure

## Tuples can store any data types
## Tuple is similar to list, but is "immutable" meaning that its elements cannot be changed or modified after the tuple is created
## No append(), no pop(), no insert(), no remove()
## Tuples are faster than lists

##* Tuples are defined using parentheses () and elements are separated by commas
## 01: Creating tuples using parentheses ():

# Creating a tuple of integers
my_tuple = (1, 2, 3, 4, 5)

# Creating a tuple of strings
fruits = ('apple', 'banana', 'cherry')

# Creating a tuple with mixed data types
mixed_tuple = (1, 'apple', 3.14, True)


## 02: Creating tuple without parenthesis:
my_tuple2 = 1, 2, 3, 4
print(my_tuple2)  # (1, 2, 3, 4)
print(type(my_tuple2))  # <class 'tuple'>


##* Accessing Elements: Elements in a tuple are accessed using indexing, similar to lists.
fruits = ('apple', 'banana', 'cherry')

print(fruits[0])  # Output: 'apple' (first element)
print(fruits[-1]) # Output: 'cherry' (last element)


##* Immutable Nature: Once created, the elements of a tuple cannot be modified.
fruits = ('apple', 'banana', 'cherry')

# Attempting to modify an element will raise a TypeError
# fruits[0] = 'orange'  # This will raise a TypeError


##* Tuple Packing and Unpacking:
# 01: Tuple packing involves creating a tuple without using parentheses.
# 02: Tuple unpacking allows assigning individual elements of a tuple to separate variables.

# Tuple packing
my_tuple = 1, 2, 3
print(my_tuple)  # Output: (1, 2, 3)

# Tuple unpacking
x, y, z = my_tuple
print(x)  # Output: 1
print(y)  # Output: 2
print(z)  # Output: 3


##* Single-Element Tuple: To create a single-element tuple, a comma , is required after the element.
# Single-element tuple
single_tuple = (42,)
print(single_tuple)  # Output: (42,)

# without comma - it will consider it as single value of respective data type
t = (42)
print(t) # 42
print(type(t)) # <class 'int'>


##* looping through tuple - similar to lists
# Example 1: Looping through a tuple of integers
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item)
# Output:
# 1
# 2
# 3
# 4
# 5

# Example 2: Looping through a tuple of strings
fruits = ('apple', 'banana', 'cherry')
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Example 3: Looping through a tuple with mixed data types
mixed_tuple = (1, 'apple', 3.14, True)
for element in mixed_tuple:
    print(element)
# Output:
# 1
# apple
# 3.14
# True


##* list inside tuple

# Tuple with a list inside
tuple_with_list = (1, 2, ['a', 'b', 'c'], 4, 5)

# Accessing elements of the tuple and the list inside it
print(tuple_with_list[0])       # Output: 1
print(tuple_with_list[2])       # Output: ['a', 'b', 'c']
print(tuple_with_list[2][1])    # Output: 'b'

# modifying list inside tuple
# NOTE: we can mutate the list inside tuple
print(tuple_with_list[2].pop())  # Output: 'c'
tuple_with_list[2].append('d')
print(tuple_with_list)  # (1, 2, ['a', 'b', 'd'], 4, 5)


##* min(), max() and sum() methods

## 01 Using min(), max(), and sum() with Tuples of Numbers:
# Tuple of numbers
numbers = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3)

# Find the minimum value
minimum = min(numbers)
print("Minimum value:", minimum)  # Output: Minimum value: 1

# Find the maximum value
maximum = max(numbers)
print("Maximum value:", maximum)  # Output: Maximum value: 9

# Compute the sum of all elements
total = sum(numbers)
print("Sum of all elements:", total)  # Output: Sum of all elements: 39


## 02 Using min(), max(), and sum() with Tuples of Strings (Lexicographic Order):
# Tuple of strings
words = ("apple", "banana", "cherry", "date")

# Find the minimum string (lexicographically)
min_word = min(words)
print("Minimum word:", min_word)  # Output: Minimum word: apple

# Find the maximum string (lexicographically)
max_word = max(words)
print("Maximum word:", max_word)  # Output: Maximum word: date


## 03 Using min(), max(), and sum() with Empty Tuples:
# Empty tuple
empty_tuple = ()

# For min() and max(), empty tuple raises ValueError
try:
    minimum = min(empty_tuple)
except ValueError:
    print("Empty tuple has no minimum value.")
try:
    maximum = max(empty_tuple)
except ValueError:
    print("Empty tuple has no maximum value.")

# For sum(), empty tuple results in 0
total = sum(empty_tuple)
print(
    "Sum of elements in an empty tuple:", total
)  # Output: Sum of elements in an empty tuple: 0


##* sorted() method with tuple

## 01 Sorting a Tuple of Numbers:
# Tuple of numbers
numbers = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3)

# Sort the tuple
sorted_numbers = sorted(numbers)
print(
    "Sorted numbers:", sorted_numbers
)  # Output: Sorted numbers: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]


## 02 Sorting a Tuple of Strings (Lexicographic Order):
# Tuple of strings
words = ("apple", "banana", "cherry", "date")

# Sort the tuple
sorted_words = sorted(words)
print(
    "Sorted words:", sorted_words
)  # Output: Sorted words: ['apple', 'banana', 'cherry', 'date']

## 03 Sorting a Tuple of Mixed Data Types:
# Tuple of mixed data types
mixed_data = (3, "apple", 1.5, "banana", 2.5)

# Sort the tuple
# sorted_mixed_data = sorted(mixed_data)  # TypeError

## 04 Sorting a Tuple in Reverse Order:
# Tuple of numbers
numbers = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3)

# Sort the tuple in reverse order
sorted_numbers_reverse = sorted(numbers, reverse=True)
print(
    "Sorted numbers in reverse order:", sorted_numbers_reverse
)  # Output: Sorted numbers in reverse order: [9, 6, 5, 5, 4, 3, 3, 2, 1, 1]


##* tuple() method to convert other types to tuple

## 01 Converting a List to a Tuple:
# List
my_list = [1, 2, 3, 4, 5]

# Convert list to tuple
my_tuple = tuple(my_list)
print("Tuple:", my_tuple)  # Output: Tuple: (1, 2, 3, 4, 5)

## 02 Converting a String to a Tuple (Characters):

# String
my_string = "hello"

# Convert string to tuple of characters
my_tuple = tuple(my_string)
print("Tuple:", my_tuple)  # Output: Tuple: ('h', 'e', 'l', 'l', 'o')


## 03 Converting range() to tuple
my_tuple = tuple(range(10))
print("Tuple:", my_tuple)  # Output: Tuple: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


##* return multiple values from function
# tuple without parenthesis is used to return multiple values from function

def calc(num1, num2):
    sum = num1 + num2
    mult = num1 * num2
    return sum, mult

res = calc(10, 20)
print(res)  # Output: (30, 200)
print(type(res))  # Output: <class 'tuple'>

# unpacking tuple
sum, mult = calc(12, 12)
print(sum, mult)  # 24 144