## buil-in dictionary methods

##* keys(): Returns a view object that displays a list of all the keys in the dictionary.
my_dict = {"a": 1, "b": 2, "c": 3}

# Get all keys
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['a', 'b', 'c'])
print(type(keys))  # <class 'dict_keys'>

# dict_keys is an iterable
## 01 we can iterate through using loop
for key in keys:
    print(key)  # a, b, c -> dict keys
    print(my_dict[key])  # 1, 2, 3 -> dict values

## 02 convert to other common iterables like list, tuple
print(list(keys))  # ['a', 'b', 'c']
print(tuple(keys))  # ('a', 'b', 'c')


##* values(): Returns a view object that displays a list of all the values in the dictionary

my_dict = {"a": 1, "b": 2, "c": 3}

# Get all values
values = my_dict.values()
print(values)  # Output: dict_values([1, 2, 3])
print(type(values))  # <class 'dict_values'>

# dict_values is also an iterable like dict_keys
# 01: we can loop over using loop
# 02: convert to commonly used iterables like list or tuple

## Check if value exists in the dictionary: using 'in' keyword and .values()
if 2 in values:
    print("Value exists")
else:
    print("Value doesn't exist")
# Output: Value exists

if "Something" in {"key1": "Something"}.values():
    print("Yes, exists!")
# Output: Yes, exists!

##* items(): Returns a view object that displays a list of tuples representing key-value pairs in the dictionary.
my_dict = {"a": 1, "b": 2, "c": 3}

# Get all key-value pairs
items = my_dict.items()
print(items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])
print(type(items))  # Output: <class 'dict_items'>

# dict_items is also an iterable like dict_keys and dict_values
## looping through dict_items:

for item in items:
    print(item)
# Output: NOTE- it is a list of tuples
# ('a', 1)
# ('b', 2)
# ('c', 3)

## we can unpack tuple -
for key, value in items:
    print(f"{key}: {value}")


##* popitem() - used to delete last added entry from dictionary, it returns tuple containing key value

my_dict = {"a": 1, "b": 2, "c": 3}

# Remove and return an arbitrary (key, value) pair
removed_item = my_dict.popitem()
print("Removed item:", removed_item)  # Output: Removed item: ('c', 3)

print("Updated dictionary:", my_dict)  # Output: Updated dictionary: {'a': 1, 'b': 2}

# NOTE:  the specific item removed is not guaranteed in dictionaries created before Python 3.7.


##* get(key[, default]): Returns the value associated with the specified key. If the key does not exist, it returns the optional default value or None if not provided.
## NOTE: get method does not return KeyError, unlike [] operator

my_dict = {"a": 1, "b": 2, "c": 3}

# Get value for key 'a'
value_a = my_dict.get("a")
print(value_a)  # Output: 1

# Get value for key 'd' (which doesn't exist)
value_d = my_dict.get("d")
print(value_d)  # Output: None

# Get value for key 'd' with default value 0
value_d_default = my_dict.get("d", 0)
print(value_d_default)  # Output: 0


##* update(iterable): Updates the dictionary with elements from another dictionary or iterable object (e.g., another dictionary, list of tuples).

my_dict = {"a": 1, "b": 2}

# Update dictionary with another dictionary
my_dict.update({"c": 3, "d": 4})
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Update dictionary with a list of tuples
my_dict.update([("e", 5), ("f", 6)])
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}


##* copy(): create and returns shallo copy of dictionary

my_dict = {"a": 1, "b": 2}

# Clear the dictionary
my_d_copy = my_dict.copy()
print(my_d_copy)  # Output: {'a': 1, 'b': 2}
print(my_d_copy is my_dict)  # Output: False
print(my_d_copy == my_dict)  # Output: True
print(my_dict is my_d_copy)  # Output: False

##* clear(): Removes all items from the dictionary.

my_dict = {"a": 1, "b": 2}

# Clear the dictionary
my_dict.clear()
print(my_dict)  # Output: {}
