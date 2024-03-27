## Scope refers to the region of the code where variable is accessible

##* Types of scope: global scope, local scope, and nonlocal scope

# Global Scope:
# Variables defined outside of any function have global scope.
# Global variables are accessible from anywhere in the code, including inside functions.

## Example:

x = 10  # Global variable

def my_function():
    print(x)  # Accessing global variable

my_function()  # Output: 10


# Local Scope:
# Variables defined inside a function have local scope.
# Local variables are only accessible within the function where they are defined.

# Example:

def my_function():
    y = 20  # Local variable
    print(y)

my_function()  # Output: 20
# print(y)  # This will raise a NameError because y is not defined in the global scope


# Shadowing:
# When a local variable has the same name as a global variable, it "shadows" the global variable within the local scope.
# The global variable remains accessible outside the function, but within the function, the local variable takes precedence.

## Example:
z = 30  # Global variable

def my_function():
    z = 40  # Local variable with the same name as global variable
    print(z)  # Accessing local variable

my_function()  # Output: 40
print(z)  # Output: 30 (Global variable is unaffected)


# Nonlocal Scope:
# Variables defined in an enclosing function's scope (but not in the global scope) can be accessed using the nonlocal keyword.
# This is useful for modifying variables in an outer function's scope from within an inner function.

## Example:
def outer_function():
    count = 0  # Variable in outer function's scope

    def inner_function():
        nonlocal count
        count += 1  # Modifying variable from outer scope
        print(count)

    inner_function()  # Output: 1
    inner_function()  # Output: 2

outer_function()
