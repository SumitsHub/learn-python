##* empty string
print(bool(""))  # False

##* 0
print(bool(0))  # False

##* empty list
print(bool([]))  # False

##* empty tuple
print(bool(()))  # False

##* empty set/dictionary
print(bool({}))  # False

##* string 0
print(bool("0"))  # True

##* non-empty values
print(bool("Somehting"))  # True
print(bool(20))  # True
print(bool([1, 2, 3]))  # True
print(bool({1, 2, 3}))  # True
print(bool((1, 2, 3)))  # True
print(bool({"k1": "val1", "k2": "val2"}))  # True
