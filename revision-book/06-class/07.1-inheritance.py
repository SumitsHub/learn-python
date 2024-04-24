
#* MRO - Method Resolution Order
class Parent1:
    pass

class Parent2:
    pass

class Child1(Parent1):
    pass

class Child2(Parent1, Parent2):
    pass

# print(help(Child1)) # prints MRO of class
# Output:
# Help on class Child1 in module __main__:

# class Child1(Parent)
#  |  Method resolution order:
#  |      Child1
#  |      Parent1
#  |      builtins.object
#  |
#  |  Data descriptors inherited from Parent:
#  |
# -- More  --

#* mro() and __mro__()
print(Parent1.mro())  # [<class '__main__.Parent1'>, <class 'object'>]
print(Child1.mro())  # [<class '__main__.Child1'>, <class '__main__.Parent1'>, <class 'object'>] - prints list (Left to Right order)
print(Child2.__mro__)  # (<class '__main__.Child2'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>) - prints tuple (Left to Right order)

#* isinstance() and issubclass()
# 01: isinstance() - 
#* Syntax: "isinstance(object, class_or_tuple)" returns True if the object is an instance of the specified class or any of its subclasses (if a tuple of classes is provided), otherwise it returns False.
# It's commonly used to check if an object belongs to a certain class or type.

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

print(isinstance(dog, Dog))      # Output: True
print(isinstance(cat, Animal))   # Output: True (Cat is subclass of Animal)
print(isinstance(cat, Dog))      # Output: False
print(isinstance(cat, (Animal, Dog)))      # Output: True - tuple passes as second argument


#02: issubclass() -
#* Syntax: "issubclass(subclass, superclass)" - returns True if the subclass is indeed a subclass of the superclass, otherwise it returns False.
# It's used to check if a class is a subclass of another class.

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Bird:
    pass

print(issubclass(Dog, Animal))   # Output: True
print(issubclass(Cat, Animal))   # Output: True
print(issubclass(Dog, Bird))     # Output: False
