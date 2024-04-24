
#* Dunder methods - Dunder methods, also known as magic methods or special methods, are predefined methods in Python classes that have double underscores (__) at the beginning and end of their names.
# These methods allow classes to emulate built-in behavior and interact with Python's syntax and operators. 


# Here are some common dunder methods and their purposes:

#* 01 '__init__': This method is called when an object is created. It initializes the object's attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)

#* 02 '__str__': This method is called when the str() function is used on an object. It should return a string representation of the object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

person = Person("Alice", 30)
print(str(person))  # Output: Name: Alice, Age: 30
print(person)  # Name: Alice, Age: 30


#* 03 '__repr__': This method is called when the repr() function is used on an object or when the object is displayed in the REPL(Read Eval Print Loop). It should return an unambiguous representation of the object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 30)
print(repr(person))  # Output: Person(name='Alice', age=30)
print(person)  # Person(name='Alice', age=30)

# Try creating child class and print it
class Person2(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
print(Person2('Alice', 87))  # Person(name='Alice', age=87)

#* '__len__': This method is called when the len() function is used on an object. It should return the length of the object.
class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))  # Output: 5


#* '__add__': This method is called when the + operator is used on objects. It should implement addition behavior.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
result = v1 + v2
print(result.x, result.y)  # Output: 4 6
