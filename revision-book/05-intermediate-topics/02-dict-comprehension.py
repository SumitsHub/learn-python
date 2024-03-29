## Dictionary comprehension (DC)
#  provides a concise way to create dictionaries from an iterable by specifying both keys and values using a compact syntax

# Syntax: 
#* new_dict = { key_expression: value_expression for item in iterable if condition }
## key_expression: Expression to compute keys for the dictionary.
## value_expression: Expression to compute values for the dictionary.
## item: Variable representing each item in the iterable.
## iterable: Existing iterable (e.g., list, tuple, range) from which to extract items.
## if condition (optional): Condition to filter items. Only items for which the condition evaluates to True will be included in the dictionary.


##* Creating a Dictionary of Squares:

# Using dictionary comprehension
square_dict = {x: x*x for x in range(1, 6)}
print(square_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


##* Creating a Dictionary from a List with Condition:

# List with even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using dictionary comprehension to create a dictionary with only even numbers
even_dict = {num: num * num for num in numbers if num % 2 == 0}
print(even_dict)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


##* Creating a Dictionary with Conditional Values:

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using dictionary comprehension to categorize numbers as even or odd
number_category = {num: 'even' if num % 2 == 0 else 'odd' for num in numbers}
print(number_category)  # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

##* Converting a Dictionary to Uppercase:

# Dictionary with lowercase keys and values
my_dict = {'hello': 'world', 'python': 'programming'}

# Using dictionary comprehension to convert keys and values to uppercase
uppercase_dict = {key.upper(): value.upper() for key, value in my_dict.items()}
print(uppercase_dict)  # {'HELLO': 'WORLD', 'PYTHON': 'PROGRAMMING'}