## Operators used with conditional statements

##* 'and' and 'or' operators
# NOTE: && and || operators are not available in python

age = int(input('Enter your age to proceed: '))

if age >= 18 and age < 50:
    print('You are young adult')
else:
    print('Condition didn\'t match')


if age < 18 or age > 50:
    print('Sorry! You can\'t proceed' )
else:
    print('You can go ahead!')



##* 'in' keyword - returns true if left operand is present in the right operand

# check in string
if "a" in "Capital":
    print("a is present")  # it's the output
else:
    print("a is not there")

# NOTE: 'in' operator is case-sensitive
if "cat" in ["Dog", "Cat", "Elephant"]:
    print("cat found")
else:
    print("cat not found")  # -> output


# check in list
if 3 in [1, 2, 3, 4]:
    print("3 is present")  # it's the output

if "apple" in ["banana", "apple", "orange", "pomogrenate"]:
    print("apple found")  # -> output
   
