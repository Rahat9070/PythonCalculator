class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        return base ** exponent
    
    def square_root(self, value):
        if value < 0:
            raise ValueError("Cannot take square root of a negative number")
        return value ** 0.5
    
    def modulus(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulus by zero")
        return a % b
    
    
    