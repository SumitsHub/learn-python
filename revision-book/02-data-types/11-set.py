## Set - Unordered collection of unique values
# Sets are mutable, meaning you can add or remove elements from them, but they do not support indexing or slicing like lists do
# Set can only store primary data types - we can't store list, tuple, dict inside any set

##* Creating a Set: Sets are created using curly braces {}.

# Creating an empty set
empty_set = set()

# Creating a set with elements
my_set = {1, 2, 3, 4, 5}

# Creating a set from a list (removes duplicates)
my_list = [1, 2, 3, 3, 4, 5]
my_set_from_list = set(my_list)

print(my_set_from_list)  # Output: {1, 2, 3, 4, 5}
print(type(my_set_from_list))  # <class 'set'>


##* Adding and Removing Elements: You can add elements to a set using the add() method, and remove elements using the remove() or discard() method.
my_set = {1, 2, 3}

# Adding an element
my_set.add(4)

# Removing an element, KeyError if not exists
my_set.remove(2)

# Removing an element if it exists (no error if element doesn't exist)
my_set.discard(5)

##* clear() - clears set, copy() - creates shallow copy

my_set = {1, 2, 3}

my_set.clear()
print(my_set)  # set() -> NOTE: empty set representation

my_set = {1, 2, 3}
my_set_copy = my_set.copy()
print(my_set_copy)  # {1, 2, 3}
print(my_set == my_set_copy)  # True
print(my_set is my_set_copy)  # False

##* Set Operations | Set Maths: Sets support various operations such as union, intersection, difference, and symmetric difference.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1 | set2  # or set1.union(set2)
print(union_set)  # {1, 2, 3, 4, 5}

# Intersection
intersection_set = set1 & set2  # or set1.intersection(set2)
print(intersection_set)  # {3}

# Difference
difference_set = set1 - set2  # or set1.difference(set2)
print(difference_set)  # {1, 2}

# Symmetric difference (elements present in one set but not both)
symmetric_difference_set = set1 ^ set2  # or set1.symmetric_difference(set2)
print(symmetric_difference_set)  # {1, 2, 4, 5}


##* Iterating Through a Set: You can iterate through elements of a set using a for loop.
my_set = {1, 2, 3}

for element in my_set:
    print(element)
# Output: 1 2 3


##* Built-in methods
my_set = {1, 2, 3}

# Check if element exists
print(1 in my_set)  # Output: True

# Get length of set
print(len(my_set))  # Output: 3
