##* Function Docstrings
# * What are docstrings?
# A string literal that occurs as the first statement in a function and is used to document what the function does, its parameters, return values, and any other relevant information.
# The docstring is enclosed in triple quotes (""") and is placed immediately after the function definition.


# Example:
def greet(name):
    """
    This function greets the user with the given name.

    Parameters:
    name (str): The name of the user to greet.

    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"


# * How to access docstrings?
# Function docstrings are accessible via the __doc__ attribute of the function object.

print(greet.__doc__)
# Output:
#     This function greets the user with the given name.

#     Parameters:
#     name (str): The name of the user to greet.

#     Returns:
#     str: A greeting message.


# accessing doc string of built-in method
print(len.__doc__)  # Return the number of items in a container.
print(map.__doc__)
# Output:
# map(func, *iterables) --> map object

# Make an iterator that computes the function using arguments from
# each of the iterables.  Stops when the shortest iterable is exhausted.

# * help() - get help on buil-in functions
help(
    sum
)  # returns None and prints info abput input buil-in function (similar to print(sum.__doc__))
# Output:
# Help on built-in function sum in module builtins:

# sum(iterable, /, start=0)
# Return the sum of a 'start' value (default: 0) plus an iterable of numbers

# When the iterable is empty, return the start value.
# This function is intended specifically for use with numeric values and may
# reject non-numeric types.
