## General String and List methods

seperator = ', '

##* split(sep: LiteralString | None = None, maxsplit: SupportsIndex = -1) -> list[LiteralString]
# Return a 'list' of the substrings in the 'string', using sep as the separator string.

fruits_list = 'banana, orange, apple'.split(seperator)  # splitting string by ', '
print(fruits_list)  # Output: ['banana', 'orange', 'apple']


##* join() - Concatenate any number of strings.

fruits = seperator.join(fruits_list)
print(fruits)  # Output: banana, orange, apple


##* range() - generating list using range method

# type of range() return - <class 'range'>
print(type(range(10)))

# generate numbers from 1 to 10
numbers = list(range(1, 11))  # using list() to convert range object to list
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]