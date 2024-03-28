## Dictionary - Unordered collections of data in key:value pair

##*Creating a Dictionary: Dictionaries are created using curly braces {} and key-value pairs.

# Creating an empty dictionary
empty_dict = {}

# Creating a dictionary of person's details
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Creating a dictionary with different data types
mixed_dict = {'key': 10, 5: 'value', (1, 2): ['a', 'b']}

print(person)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(type(person))  # <class 'dict'>

#* create dictionary with dict()
user = dict(name= 'Hardik', age=34)
print(user)  # {'name': 'Hardik', 'age': 34}


##* Accessing Elements: Elements in a dictionary are accessed using keys.
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

print(person['name'])  # Output: Alice
print(person['age'])   # Output: 30


##* Adding or Modifying Elements: You can add new key-value pairs or modify existing ones.
person = {'name': 'Alice', 'age': 30}

# Adding a new key-value pair
person['city'] = 'New York'

# Modifying an existing value
person['age'] = 31

print(person)  # {'name': 'Alice', 'age': 31, 'city': 'New York'}


##* Removing Elements: You can remove key-value pairs using the 'del' keyword or the 'pop()' method.
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Deleting a key-value pair
del person['age']

# Removing and returning the value of a specific key
city = person.pop('city')
print(city)  # New York


##* 'in' keyword with dictionary - checks if key exists in the dictionary
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

print('city' in person)  # True

var = 'age'
if var in person:
    print(f'{var} key is present in the person')
else:
    print(f'{var} key isn\'t present in the person')
# Output: age key is present in the person
