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