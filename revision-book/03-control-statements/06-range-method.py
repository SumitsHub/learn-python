
##* range() function - used to generate a sequence of numbers

# Syntax: range(stop)
# Generates numbers from 0 up to (but not including) the stop value
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

## Specifying start and stop value - 
    
# Syntax: range(start, stop)
# Generates numbers from start (inclusive) up to (but not including) the stop value
for i in range(2, 5):
    print(i)  # Output: 2, 3, 4

## Specifying step value - 

# Syntax: range(start, stop, step)
# Generates numbers from start (inclusive) up to (but not including) the stop value, with a specified step
for i in range(0, 10, 2):
    print(i)  # Output: 0, 2, 4, 6, 8


## creating list using range() -
    
# You can use the list() function to convert a range object to a list
numbers = list(range(5))
print(numbers)  # Output: [0, 1, 2, 3, 4]


## negative step value -

# Using a negative step value to generate numbers in descending order
for i in range(5, 0, -1):
    print(i)  # Output: 5, 4, 3, 2, 1


# It's important to note that in Python 3, range() returns a "range object", which is an immutable sequence type, rather than generating the entire sequence of numbers at once. 
# This makes range() memory-efficient, especially when dealing with large ranges.