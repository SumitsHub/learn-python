##* type() function in Python

## type() function returns type of value stored in the input variable or input

name = 'John'
print(type(name)) # <class 'str'>
print(type('Hello')) # <class 'str'>


age = 25
print(type(age)) # <class 'int'>

temp = 23.5
print(type(temp)) # <class 'float'>

def test():
    print('Heyy')


# type of function is function
print(type(test)) # <class 'function'>

# type of lambda function is also a function
print(type(lambda x:x)) # <class 'function'>

class Animal:
    def __init__(self) -> None:
        pass

print(type(Animal)) # <class 'type'>

print(type(Animal())) # <class '__main__.Animal'>


##* len() function - returns length of enumerable
# length of string
print(len("Something"))  # 9
# length of list
print(len([1, 2, 3, 4, 5]))  # 5
# length of tupple
print(len((1, 2, 3, 4, 5)))  # 5

# length of set
print(len({1, 2, 3, 4, 5, 5, 6, 6})) # 6 -> NOTE: doesn't count duplicates
# with dictionary
print(len({'k1': 'Something', 'k2': 'Something'})) # 2 -> return number of keys for Dictionary