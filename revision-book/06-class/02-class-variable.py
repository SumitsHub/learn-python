
##* class variables -  class variables are variables that are shared among all instances of a class. They are defined within the class definition but outside of any method


class Dog:
    species = 'Canis familiaris'  # Class variable
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Milo", 5)

# Accessing class variable
print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris

# Class variables can also be accessed via the class itself
print(Dog.species)   # Output: Canis familiaris


##* magic variable
print(dog1.__dict__)  # {'name': 'Buddy', 'age': 3}  # NOTE: this didn't contain class variable

print(Dog.__dict__)  # {'__module__': '__main__', 'species': 'Canis familiaris', '__init__': <function Dog.__init__ at 0x00000266C5478E00>, '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None}
# NOTE: __dict__ for class contains class variables (e.g. 'species': 'Canis familiaris')