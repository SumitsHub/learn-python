
#* @property decorator - property decorator in Python is a built-in decorator that allows you to define methods that can be accessed like attributes. 

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter method for radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter method for radius."""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @radius.deleter
    def radius(self):
        """Deleter method for radius."""
        del self._radius

# Example usage
circle = Circle(-5)  # NOTE: setter is not called while setting through constructor
print(circle.radius)  # Output: -5

circle.radius = 10
# circle.radius = -10  # ValueError: Radius must be positive NOTE: setter raised the error
print(circle.radius)  # Output: 10

del circle.radius
# Accessing it after deletion will raise an AttributeError
