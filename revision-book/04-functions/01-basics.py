
##* defining functions in pythong

## Syntax: 
# def func_name(paramters):
#     pass # function body

n1 = int(input('Enter number #01: '))
n2 = int(input('Enter number #02: '))

## Examples: 
# 01: function to add 2 numbers
def add(num1, num2):
    print(f'{num1} + {num2} = {num1 + num2}')

add(n1, n2)  # 12 + 21 = 33

# 02: funtion returning multiplication of 2 nums
def mult(num1, num2):
    return num1 * num2

res = mult(n1, n2)
print(f'{n1} * {n2} = {res}')  # 12 * 21 = 252
# OR
print(f'{n1} * {n2} = {mult(n1, n2)}')  # 12 * 21 = 252

# 03: nesting functions
def is_even(num):
    """
    function to return True if input is an even number, False otherwise
    """
    return num % 2 == 0

def is_odd(num):
    """
    function to return True if input is odd number, False otherwise
    """
    return num % 2 != 0

# using above two functions inside new one too determine if number is odd or even
def odd_even(num):
    if is_even(num):
        return 'Even Number'
    elif is_odd(num):
        return 'Odd Number'
    else:
        return 'Something weird'
    
print(odd_even(0))  # Even Number
print(odd_even(12))  # Even Number
print(odd_even(15))  # Odd Number
