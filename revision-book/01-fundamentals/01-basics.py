# This is commente and will be ignored by python interpreter
# Comment starts with # symbol in Python

##* print function

print("Hello")  # single quote string

print("Hello")  # double quote string

print("Hey I't me..")  # single quote inside double quote

print('Hey I am "BIG" start..')  # double quote inside single quote

##* Escape  Sequences
# \" - double quote
print(
    'Heyy there "listen" to me'
)  # using double quotes inside duoble quote using escape sequences

# \' - single quote
print("Heyy thete ' listen' to me")

# \\
print("This is example of \\back slash")

# \n
print("This will be print on \nnew line")

# \t
print("This is \t tab")

# \b
print("This is \b backspace")


##* Escape sequence as normal text
print("Line A \\n Line B")  # Output: Line A \n Line B


##* Raw Strings - string starting with letter 'r', treats escape sequences as normal text

print(r"Line A \n Line B")  # Output: Line A \n Line B



##* Variables in Python

# Creating variables - no need to specify data type and no need to use any keyword like other programming languages
name = 'Steve'
print(name)  # printing value of variable

# NOTE: you can't create variables without values unlike other programming language

# Dynamic programming language - type of variable is determined at the run time based on the value assigned to the variable
# Python is dynamic programming language

name = 123  # storing integer value, initially stored string value
print(name)

full_name = 'John Doe'  # snake case naming convention is followed 

# creating multiple variables in one line
name, age = 'John', 30  
print(name, age)  # John 30


##* number of variables on left and values on the right must match
# name, age = 'John'
# print(name, age) # ValueError: too many values to unpack (expected 2)

# unpacking with array also works - can be usefull to take multiple user input in single line
num1, num2 = [10, 200]
print(num1, num2) # 10 200

# creating multiple variables with same value
x = y = z = 11
print(x, y, z) # 11 11 11