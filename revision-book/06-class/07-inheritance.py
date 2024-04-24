
#* Inheritance - a new class (subclass) can be created based on an existing class (superclass).

#* Defining Parent class: aka Superclass or Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass  # Placeholder method to be overridden in subclasses

#* Defining sub class(es)
class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"


dog = Dog("Buddy")  # creating sub class instance
print(dog.name)     # Output: Buddy  - 'name' property from parent class
print(dog.sound())  # Output: Woof! - 'sound' method from child class - got overridden

# Method overloading - Python looks for method in subclass first then go for parent class


#* Multiple Inheritance
class Bird:
    def fly(self):
        return "I can fly!"

class Parrot(Animal, Bird):
    pass

parrot = Parrot("Polly")
print(parrot.name)  # Output: Polly
print(parrot.sound())  # Output: None - (Method from Animal superclass)
print(parrot.fly())  # Output: I can fly! - (Method from Bird superclass)



#* super keyword - The super() function in Python is used to access methods and properties from a superclass. 

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Generic animal sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call superclass constructor
        # another way to call parent class constructor
        # Animal.__init__(self, name)  # uncommon way
        self.breed = breed

    def sound(self):
        return "Woof!"


# Create an instance of the Dog class
dog = Dog("Buddy", "Labrador")

# Accessing properties from the superclass using super()
print(dog.name)  # Output: Buddy

# Accessing overridden method from the superclass using super()
print(super(Dog, dog).sound())  # Output: Generic animal sound
