
##* map() function - Make an iterator that computes the function using arguments from each of the iterables.
# returns map object (iterable), we can convert to list/tuple

nums = [1, 2, 3, 4]

def square(n):
    return n ** 2

squares = map(square, nums)
print(squares)  # map object

print(list(squares))  # [1, 4, 9, 16]

#* map() stops when shortest iterable exausts

print(list(map(lambda x, y : x + y , [1, 2, 3, 4, 5, 6], [1, 2, 3, 4])))  # [2, 4, 6, 8]

print(list(map(lambda x, y, z : (x * y) - z , [1, 2, 3, 4, 5, 6], [1, 2, 3, 4], [9, 8])))  # [-8, -4]

# NOTE: number of iterables = number of input parameters to the function
# List Comprehension can be used most of the time


##* passing buil-in method to map()
names = ['Ram', 'Ghansham', 'Alicea', 'Samnatha']
name_lengths = tuple(map(len, names)) 
print(name_lengths)  # (3, 8, 6, 8)
