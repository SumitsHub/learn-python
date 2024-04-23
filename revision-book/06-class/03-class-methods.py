from datetime import datetime
#* class methods - different than C++ or Java Static method

class Person:
    count = 0

    def __init__(self) -> None:
        Person.count += 1

    # defining class method
    @classmethod # decorator
    def get_count(cls):
        return f"You have created {cls.count} instance of {cls.__name__} class"
    
p1 = Person()
# calling class method using Person class
print(Person.get_count())  # You have created 1 instance of Person class

p2 = Person()
print(Person.get_count())  # You have created 2 instance of Person class

# calling class method using an instance of Person class
print(p2.get_count())  # You have created 2 instance of Person class


#* class method as constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = datetime.now().year
        age = current_year - birth_year
        return cls(name, age)

# Using the regular constructor
person1 = Person("Alice", 30)
print(person1.name, person1.age)  # Output: Alice 30

# Using the class method as a constructor
person2 = Person.from_birth_year("Bob", 1990)
print(person2.name, person2.age)  # Output: Bob 34

