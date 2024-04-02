
##* zip() function

user_id = [f'u{i}' for i in range(1, 4)]
user_name = ['Rohit', 'Mohit', 'Sumit']

print(zip(user_id, user_name))  # zip object
print(list(zip(user_id, user_name)))  # [('u1', 'Rohit'), ('u2', 'Mohit'), ('u3', 'Sumit')]

print(list(zip('abcdefg', range(3), range(4))))  # [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]


## Creating dictionary from zip object using dict()
print(dict(zip('abcd', range(4))))  # {'a': 0, 'b': 1, 'c': 2, 'd': 3}

##* '*' operator with zip

l1 = list(range(4))
l2 = list(range(4))

l = list(zip(l1, l2))
print(l)  # [(0, 0), (1, 1), (2, 2), (3, 3)]
print(list(zip(*l)))  # [(0, 1, 2, 3), (0, 1, 2, 3)]
