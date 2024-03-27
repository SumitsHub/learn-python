
##* List
## a list is a data structure that represents an ordered collection of elements.
## Lists are mutable, meaning that you can change their contents after they are created
## Lists can contain elements of different data types, including integers, floats, strings, and even other lists


##* Creating Lists:
# Lists are created using square brackets [], and elements are separated by commas.

# Example:
# Creating a list of integers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ['apple', 'banana', 'cherry']

# Creating a list with mixed data types
mixed_list = [1, 'apple', 3.14, True]

##*Accessing Elements:
# Elements in a list are accessed using indexing. Indexing starts from 0 for the first element.
# Negative indices can also be used to access elements from the end of the list.

# Example:
numbers = [1, 2, 3, 4, 5]

print(numbers[0])   # Output: 1 (first element)
print(numbers[-1])  # Output: 5 (last element)


##*Slicing Lists:
# You can extract a sublist (slice) from a list using slicing notation start:stop:step.
# Omitting start and stop values defaults to the beginning and end of the list, respectively.

# Example:
numbers = [1, 2, 3, 4, 5]

print(numbers[1:4])  # Output: [2, 3, 4] (slice from index 1 to 3)
print(numbers[:3])   # Output: [1, 2, 3] (slice from start to index 2)
print(numbers[::2])  # Output: [1, 3, 5] (slice with a step of 2)


##* Slicing with step index

## 01: Basic Examples
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Extract every second element
result = numbers[::2]
print(result)  # Output: [1, 3, 5, 7, 9]

# Extract every third element starting from index 1
result = numbers[1::3]
print(result)  # Output: [2, 5, 8]

## 02: Reverse List with Negative Step:
numbers = [1, 2, 3, 4, 5]

# Reverse the list
result = numbers[::-1]
print(result)  # Output: [5, 4, 3, 2, 1]


## 03: Slice and Modify List with Step: Extract a sublist with a step size, modify it, and assign it back to the original list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Extract every second element and square it
numbers[::2] = [x**2 for x in numbers[::2]]
print(numbers)  # Output: [1, 2, 9, 4, 25, 6, 49, 8, 81, 10]


##*Modifying Lists:
# Lists are mutable, so you can modify their elements using indexing or slicing.

# Example:
numbers = [1, 2, 3, 4, 5]

numbers[2] = 10  # Modify an element
print(numbers)   # Output: [1, 2, 10, 4, 5]

numbers[1:4] = [20, 30, 40]  # Modify a slice
print(numbers)               # Output: [1, 20, 30, 40, 5]


##* using 'del' keyword to remove elements from list

numbers = [1, 2, 3, 4, 5]

# Delete the element at index 2 (value 3)
del numbers[2]
print(numbers)  # Output: [1, 2, 4, 5]

numbers = [1, 2, 3, 4, 5]

# Delete a slice from the list (elements from index 1 to 3)
del numbers[1:4]
print(numbers)  # Output: [1, 5]

numbers = [1, 2, 3, 4, 5]

# Delete the entire list
del numbers
#* print(numbers) -> NameError: name 'numbers' is not defined


##* 'in' keyword with list - used to check if a value exists within a sequence

fruits = ['apple', 'banana', 'cherry']

# Check if 'banana' is in the list
if 'banana' in fruits:
    print('Yes, banana is in the list')

# Check if 'orange' is not in the list
if 'orange' not in fruits:
    print('No, orange is not in the list')

# Output: 
# Yes, banana is in the list
# No, orange is not in the list
