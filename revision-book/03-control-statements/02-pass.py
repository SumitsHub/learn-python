
##* 'pass' statement - it's a is a null operation. It doesn't do anything and acts as a placeholder in situations where syntactically some code is required but no action needs to be taken.

day = 14

if day <= 10:
    pass
else:
    print('it is good day')


##* more examples

# 01: in a function or class definition where you plan to implement functionality later:
def my_function():
    pass  # Placeholder for future implementation

class MyClass:
    def my_method(self):
        pass  # Placeholder for future implementation


# 02: When defining a class or function, the pass statement can be used to create a minimal valid structure before adding functionality
class MyClass:
    pass

def my_function():
    pass


# 03: In some cases, you may want to create an infinite loop that doesn't do anything. You can use the pass statement to achieve this:
while True:
    pass  # Do nothing, infinite loop
