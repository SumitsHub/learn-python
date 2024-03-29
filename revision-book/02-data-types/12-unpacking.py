
##* Unpacking: 
# Unpacking in Python refers to the process of extracting elements from iterables like lists, tuples, or dictionaries into individual variables or function arguments. 
# It allows you to assign the values of an iterable to multiple variables at once or pass them as arguments to a function.

##* Iterable Unpacking:

## 01: Unpacking a Tuple
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c)  # Output: 1 2 3

# Unpacking Tuple as Function Arguments:
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

my_tuple = ('Alice', 30)
greet(*my_tuple)  # Output: Hello, Alice! You are 30 years old.


## 02: Unpacking a List
my_list = [4, 5, 6]
x, y, z = my_list
print(x, y, z)  # Output: 4 5 6


# Unpacking List as Function Arguments:
def add(a, b, c):
    return a + b + c

my_list = [1, 2, 3]
result = add(*my_list)  # unpacking using '*' operator
print(result)  # Output: 6


## 03: Unpacking a String
my_string = "hello"
a, b, c, d, e = my_string
print(a, b, c, d, e)  # Output: h e l l o



##* Dictionary Unpacking:

## 01: Unpacking Dictionary into Variables
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
name, age, city = my_dict.values()
print(name, age, city)  # Output: Alice 30 New York


## 02: Unpacking Dictionary as Keyword Arguments
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

my_dict = {'name': 'Alice', 'age': 30}
greet(**my_dict)  # Output: Hello, Alice! You are 30 years old.


##* Mixed Unpacking
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

person_info = ['Alice', 30]
city_info = {'city': 'New York'}

# Unpacking a list and a dictionary together
describe_person(*person_info, **city_info)  # Output: Alice is 30 years old and lives in New York.
