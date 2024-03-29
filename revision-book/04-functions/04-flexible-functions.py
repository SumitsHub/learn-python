
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
