
#* Name mangling - is a mechanism in Python that modifies the name of a variable or method in a class to make it harder to accidentally override in subclasses.
# This is achieved by prefixing the variable or method name with a double underscore (__). When Python encounters a double underscore name in a class definition, it automatically performs name mangling.

# When you define a variable or method with a name starting with two underscores (__) but not ending with two or more underscores, Python internally changes the name to include the class name. The transformation is performed by adding _ClassName to the beginning of the name.

class MyClass:
    def __init__(self):
        self.__private_var = 42

    def __private_method(self):
        return "Hello, World!"

obj = MyClass()
# Accessing the mangled variable
print(obj._MyClass__private_var)  # Output: 42
# Accessing the mangled method
print(obj._MyClass__private_method())  # Output: Hello, World!

# print(obj.__private_method())  # ERROR: AttributeError: 'MyClass' object has no attribute '__private_method'

# Since Python doesn't have true private members, name mangling provides a way to create pseudo-private members.