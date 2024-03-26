##* String in Python

# String - collection of characters inside single or double quote

# examples -
name = "Stephen"

full_name = "Stephen Grider"

para = "This is long paragraph"

# printing values
print(name, full_name, para)


##* operations with Strings

## String concatenation - addition of string refers to concatenation
s = "Hello" + "World"
print(s)  # Hello World

# print('Hello ' + 4)  # Error: TypeError: can only concatenate str (not "int") to str
print("Hello " + "4")  # Hello 4
print("Hello " + str(4))  # Hello 4 -> str() function is used to convert 'int' to 'str' (string)

## Multiplication with String
print("Hello " * 4)  # Hello Hello Hello Hello


##* String formatting

# format() function
name, age = 'John', 30
print('This is {} and I am {} years old.'.format(name, age))

# using keys in placeholders - note: it's must to pass keys in format function else will get KeyError
print('This is {n} and I am {a} years old.'.format(n = name, a = age))

##* formatted strings - starts with f followed by string
# using variables inside string directly
print(f'Hello {name} your age is {age}')
