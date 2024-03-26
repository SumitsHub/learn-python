##* Taking user input in Python

# input() function is used to accept user inputs in python
# input() function always returns user input as string type
# input() function takes optional prompt string as input argument

name = input('Enter your name: ')
print('Hello ' + name)

# Output: 
# Enter your name: John -> here John is user input
# Hello John

age = input('Enter your age: ')
print('Your age is ' + age)

# Output:
# Enter your age: 24
# Your age is 24

print(type(age)) # <class 'str'>

# input without any prompt
temp = input()
print('todays temperature is ' + temp)


# converting input from 'str' to required data type on the fly
age = int(input('Enter your age please: '))
# print('Your age is ' + age)  # TypeError: can't concatenate str with int
print(type(age)) # <class 'int'>

# Note: similar to int(), float() can also be used

# adding 2 numbers
num1 = int(input('Enter num #1: '))
num2 = int(input('Enter num #2: '))
total = num1 + num2

print('Total of input numbers is ' + str(total))
# Output:
# Enter num #1: 12
# Enter num #2: 23
# Total of input numbers is 35