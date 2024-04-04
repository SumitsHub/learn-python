
##* First class functions - functions can be treated like any other object, such as integers, strings, or lists. Specifically, this means that functions can be passed as arguments to other functions, returned as values from other functions, assigned to variables, and stored in data structures.


def square(num):
    return num ** 2

s = square  # assigning function to a variable
print(s(7))  # 49

print(s)  # <function square at 0x000001B20DAB04A0>
print(square)  # <function square at 0x000001B20DAB04A0>
# NOTE: both 'square' and 's' pointing to same location

print(s.__name__)  # square
print(square.__name__)  # square


##* Function as argument
# passing 'square' function as argument to 'map' function
print(list(map(square, [1, 2, 3])))  # [1, 4, 9]
# map with 2 iterables
print(list(map(lambda x, y : x * y, [1, 2, 3], [4, 5, 6])))  # [4, 10, 18]

# creating our own map function
def my_map(callback, iterable):
    new_list = []
    for item in iterable:
        new_list.append(callback(item))
    return new_list

print(my_map(square, [1, 2, 3]))  # [1, 4, 9]

# using list comprehension
def my_map2(callback, iterable):
    return [callback(x) for x in iterable]

print(my_map2(lambda x : x ** 3, [2, 4, 6]))  # [8, 64, 216]


##* function returning function

def outer_func(msg):
    def inner_func():
        print(f'Hello there, {msg}')
    return inner_func

func = outer_func('How are you?')
func()  # Output: Hello there, How are you?


##* Closures: inner function having access to the execution context (lexical scope) of outer function

def make_multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
