class MathOperations:
    @staticmethod  # decorator to convert a function to static method
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

# Using static methods
result1 = MathOperations.add(5, 3)
result2 = MathOperations.subtract(10, 4)

print(result1)  # Output: 8
print(result2)  # Output: 6

# static vs class method
# Static methods have no access to class variables or instance variables since they do not take 'self' or 'cls' parameters.