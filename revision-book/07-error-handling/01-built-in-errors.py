
#* 01. Syntax Error
# def func:
#     print('From func')

## Output: SyntaxError: expected '('


#* 02. Indentation Error
# def sayHello(name):
#  print(f'Hello {name}')

# sayHello('Raj')


#* 03. NameError

# print(name)  # trying to access undefined variable  
# Output: NameError: name 'name' is not defined


#* 04. TypeError

# print(5 + 'Hello')
# Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'

#* 05. IndexError

l = [1, 2, 3]
# print(l[3])
# Output: IndexError: list index out of range


#* 06. ValueError

s = '5'
print(int(s))  # 5

s = '05'
print(int(s))  # 5

s = '0x5'
# print(int(s))  #* ValueError: invalid literal for int() with base 10: '0x5'


#* 07. AttributeError

l = [1, 2, 3]
# l.add(4)  # AttributeError: 'list' object has no attribute 'add'

#* 08. KeyError

d = {'name': 'Harsh'}
# print(d['age'])  # KeyError: 'age'
