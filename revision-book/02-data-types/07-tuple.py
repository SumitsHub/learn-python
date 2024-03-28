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