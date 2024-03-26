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
