## Operators used with conditional statements

##* 'and' and 'or' operators

age = int(input('Enter your age to proceed: '))

if age >= 18 and age < 50:
    print('You are young adult')
else:
    print('Condition didn\'t match')


if age < 18 or age > 50:
    print('Sorry! You can\'t proceed' )
else:
    print('You can go ahead!')