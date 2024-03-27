## elif keyword
##* elif = else if (You can't use 'else if' in python, you need to elif)

age = int(input('Enter your age: '))

if age < 5:
    print('Ticket is free')
elif age < 10:
    print('Ticket is half')
elif age < 50:
    print('Ticket is full')
else:
    print('Ticket is half')


if age > 20:
    pass
# else if: error -> cannot use if with else, need to use elif instead
