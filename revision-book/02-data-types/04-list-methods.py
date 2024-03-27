## List methods

##* append(): Appends an element to the end of the list.

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']


##* extend(): Extends the list by appending elements from the iterable.

fruits = ['apple', 'banana', 'cherry']
fruits.extend(['grape', 'melon'])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'grape', 'melon']


##* insert(): Inserts an element at the specified index.

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')  # Insert 'orange' at index 1
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']


##* remove(): Removes the first occurrence of the specified value from the list.

fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'cherry']


##* pop(): Removes the element at the specified index (or the last element if no index is specified) and returns it.

fruits = ['apple', 'banana', 'cherry']
removed_fruit = fruits.pop(1)  # Remove and return the element at index 1 (banana)
print(removed_fruit)  # Output: 'banana'
print(fruits)         # Output: ['apple', 'cherry']


##* index(): Returns the index of the first occurrence of the specified value. 
# Raises ValuError if not found.

fruits = ['apple', 'banana', 'cherry']
index = fruits.index('banana')
print(index)  # Output: 1


##* find(): there is no built-in find method for list

# use index() method with try expect
fruits = ['apple', 'banana', 'cherry']

try:
    index = fruits.index('grape')
    print(index)
except ValueError:
    print('Value not found in the list')


##* count(): Returns the number of occurrences of the specified value.

fruits = ['apple', 'banana', 'cherry', 'banana']
count = fruits.count('banana')
print(count)  # Output: 2

##* sort(): Sorts the list in ascending order. (Note: This method modifies the original list in-place.)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]

##* reverse(): Reverses the elements of the list in-place.

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)  # Output: ['cherry', 'banana', 'apple']

