
##* Decorators - enhances functionality of other functions


def decorator_func(inp_func):
    def wrapper_func(x):
        print("This is awesome function")
        print(inp_func(x))

    return wrapper_func


func1 = decorator_func(lambda x: x**2)
func1(5)
# Output:
# This is awesome function
# 25

func2 = decorator_func(lambda x: x**3)
func2(5)

# Output:
# This is awesome function
# 125


# * @decorator_function_name - Syntactic sugar for decorator function
def decorator_func2(inp_func):
    def wrapper_func(*x):
        print("This is awesome function")
        print(inp_func(*x))

    return wrapper_func


@decorator_func2
def func3():
    return "This is from func3"


func3()
# Output:
# This is awesome function
# This is from func3


@decorator_func2
def mul(x, y):
    return x * y


mul(2, 9)
# Output:
# This is awesome function
# 18


@decorator_func2
def add(*args):
    return sum(args)


add(10, 11, 12, 13)
# Output:
# This is awesome function
# 46


# * __name__ and __doc__


def dec_fun(inp_fun):
    def wrapper():
        """This is wrapper function doc"""
        print("This is from wrapper")
        return inp_fun()

    return wrapper


@dec_fun
def test_func():
    "This is test function doc"
    return "This is from test function"


print(test_func.__name__)  # wrapper
print(test_func.__doc__)  # This is wrapper function doc



##* @wraps
# It's a helper function which preserves metadata such as the function's name, docstring, and other attributes.
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'You are calling {func.__name__}()') # You are calling add()
        print(f'{func.__doc__}')  # This function adds 2 input numbers and returns the result
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    """This function adds 2 input numbers and returns the result"""
    return a + b


print(add(2, 4))  # 6
print(add.__name__)  # add
print(add.__doc__)  # This function adds 2 input numbers and returns the result
