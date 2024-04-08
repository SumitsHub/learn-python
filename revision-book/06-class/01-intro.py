
##* 'class' in python

#* creating class

class Person:
    # constructor function
    def __init__(self, f_name, l_name, age):
        # creating instance variables
        self.f_name = f_name
        self.l_name = l_name
        self.age = age


# creating instance of class - NOTE: no 'new' keyword is used unlike other programming language
p1 = Person("Steve", "Jobs", 50)
p2 = Person("Mark", "Wood", 29)

print(p1)  # <__main__.Person object at 0x000002DFF117E9D0>
# accessing instance variables
print(p1.f_name)  # Steve
print(f"{p2.f_name} {p2.l_name} is {p2.age} years old")  # Mark Wood is 29 years old


#* instance methods

# built-in instance method (pop()) of list class
l = [1, 2, 3, 4]
print(l.pop())  # 4


# creating own instance method
class Person:
    def __init__(self, f_name, l_name) -> None:
        self.f_name = f_name
        self.l_name = l_name

    # defining instance method
    def get_full_name(self):
        return f"{self.f_name} {self.l_name}"


p = Person("Dua", "Lipa")
# calling instance method
print(p.get_full_name())  # Dua Lipa

# another way of calling using class name and passing instance of class
print(Person.get_full_name(p))  # Dua Lipa
# with list class
list.append(l, 100)
print(l)  # [1, 2, 3, 100]
