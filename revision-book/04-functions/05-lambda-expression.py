
##* Lambda Expression/Function - small anonymous function defined using the lambda keyword
## Lambda functions can have any number of arguments but can only have one expression

# * Syntax: lambda arguments: expression
# 'lambda': Keyword used to define a lambda function.
# 'arguments': Comma-separated list of input parameters (or arguments) to the function.
# 'expression': Single expression whose result is returned when the function is called.

##* Lambda Function with One Argument:
# Lambda function to double the value of its argument
double = lambda x: x * 2

# Calling the lambda function
print(double(5))  # Output: 10

##* Lambda Function with Multiple Arguments:
# Lambda function to calculate the sum of two numbers
add = lambda a, b: a + b

# Calling the lambda function
print(add(3, 4))  # Output: 7


##* Lambda Function with if else in return
is_valid = lambda s: True if len(s) > 5 else False
print(is_valid("Something"))  # Output: True


##* Practical uses of lambda functions - using lambda expression as callback functions
# *  Using Lambda with Built-in Functions:
# Using lambda with filter() to filter even numbers
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, my_list))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Using lambda with map() to square each element
squared_numbers = list(map(lambda x: x**2, my_list))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# * Sorting with Lambda
# List of tuples
my_tuples = [(1, "b"), (3, "a"), (2, "c")]

# Sorting tuples based on the first element
sorted_tuples = sorted(my_tuples, key=lambda x: x[0])
print(sorted_tuples)  # Output: [(1, 'b'), (2, 'c'), (3, 'a')]
