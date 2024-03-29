
##* Arbitrary Argument Lists (Variable-Length Arguments) || varargs || start args
# When defining functions, the * operator is used to specify variable-length argument lists (also known as "varargs" or "star args"), allowing functions to accept an arbitrary number of positional arguments

def my_function(*args):
    for arg in args:
        print(arg)

# calling function with variable number of arguments - 
my_function(1, 2, 3)  # Output: 1 2 3
my_function('a', 'b', 'c', 'd')  # Output: a b c d

# it's basically unpacking tuple
def func(*args):
    print(args)  # ('a', 1, 3, 'd')
    print(type(args))  # <class 'tuple'>

# passing arguments as a tuple without parenthesis
func('a', 1, 3, 'd')

# tuple with parenthesis
func((1, 2, 3, 4))  # complete tuple is considered as single argument in this case

#* passing list as argument
func([1, 2, 3, 4]) # complete list is considered as single argument in this case

#* unpacking tuple and list while calling function
func(*(1, 2, 3, 4, 5)) # similar to -> func(1, 2, 3, 4, 5)

func(*[1, 2, 3, 4, 5]) # similar to -> func(1, 2, 3, 4, 5)



##* *args with normal paramter

def sum_nums(num1, *args):
    return num1 + sum(args)

# calling function with normal and varargs
print(sum_nums(1, 2, 3, 4, 5, 6))  # 21

# calling only with normal args
print(sum_nums(4))  # 4

# calling without any params -> NOTE: normal params are must to pass
# print(sum_nums())  # TypeError: sum_nums() missing 1 required positional argument: 'num1'

##* NOTES:
# 01: for normal parameters - arguments must be passes
# 02: for *args - not necessary
# 03: normal parameters can't come after *args - func(*args, num1, num2) - NOT VALID
# 04: only one *args paramters is allowed
# 05: 'args' is used as name of the paramter by convention, we can use anything -  def addnum(*nums):


##* **kwargs - Keyword Arguments
# accepts named arguments are key: value pair (dictionary)

## **kwargs as parameter
def func(**kwargs):
    print(kwargs)


func(x='x', y='y', z='z')  # {'x': 'x', 'y': 'y', 'z': 'z'}

## Unpacking dictionary with '**' operator
d = {'name': 'Sham', 'age': 35}
func(**d)  # {'name': 'Sham', 'age': 35}



##* *args and **kwargs together
def func(*args, **kwargs):
    print(args, kwargs)

func(1, 2, 3, 4)  # (1, 2, 3, 4) {}
func(1, 2, name='Ram', age=24)  # (1, 2) {'name': 'Ram', 'age': 24}


##* NOTES:
# 01: **kwargs needs to be the last parameter in the list - def func(**kwargs, *args): - NOT VALID


##* About paramter types:
# Parameters need to be in the following order based on the type:
## Normal Parameters -> *args -> Named Parameters -> **kwargs

## Example function:

def all_para(roll_no, *marks, std=8, **details):
    print(f'Roll No: {roll_no}')
    print(f'Marks: {marks}')
    print(f'Class (std): {std}')
    print(f'Student details: {details}')

all_para(12, 90, 89, 88, std=10, **{'name': 'Amit', 'age': 18})
# Output:
# Roll No: 12
# Marks: (90, 89, 88)
# Class (std): 10
# Student details: {'name': 'Amit', 'age': 18}