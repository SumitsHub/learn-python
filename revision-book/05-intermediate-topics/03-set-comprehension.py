## Set Comprehension (SC) 
# provides a concise way to create sets from an iterable by specifying elements using a compact syntax

# Syntax:
#* new_set = { expression for item in iterable if condition }
# expression: Expression to compute elements for the set.
# item: Variable representing each item in the iterable.
# iterable: Existing iterable (e.g., list, tuple, range) from which to extract items.
# if condition (optional): Condition to filter items. Only items for which the condition evaluates to True will be included in the set.

##* Creating a Set of Squares
# Using set comprehension
square_set = {x * x for x in range(1, 6)}
print(square_set)  # {1, 4, 9, 16, 25}


##* Creating a Set from a List with Condition
# List with even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using set comprehension to create a set with only even numbers
even_set = {num for num in numbers if num % 2 == 0}
print(even_set)  # {2, 4, 6, 8, 10}


##* Converting a List to a Set

# List with duplicate elements
my_list = [1, 2, 3, 3, 4, 5, 5]

# Using set comprehension to remove duplicates and create a set
unique_set = {x for x in my_list}
print(unique_set)  # {1, 2, 3, 4, 5}


##* Creating a Set from a String
# String
my_string = "hello world"

# Using set comprehension to create a set of unique characters
unique_characters = {char for char in my_string}
print(unique_characters)  # {'h', ' ', 'd', 'r', 'o', 'w', 'e', 'l'}