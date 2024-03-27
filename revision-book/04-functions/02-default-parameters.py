
##* Default Paramters - allow you to specify a default value for a parameter, which is used when the function is called without providing a value for that parameter.

## Basic Example - 
def greet(name='Guest'):
    print('Hello, ' + name)

greet('John')  # Output: Hello, John
greet()        # Output: Hello, Guest


## Default with non-default paramters - 
def power(base, exponent=2):
    return base ** exponent

print(power(3))        # Output: 9 (3^2)
print(power(2, 3))     # Output: 8 (2^3)

# NOTE: default parameters must be as the end of the parameters list

# Below function definition is not valid. Error: non-default argument follows default argument
# def my_func(f_name, l_name = 'Default', age):
#     pass


##* mutable default values
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))     # Output: [1]
print(add_item(2))     # Output: [1, 2]
print(add_item(3))     # Output: [1, 2, 3]

# NOTE: because lists are mutable objects, the same list object is used as the default value every time the function is called. As a result, modifications to the default list persist across function calls.