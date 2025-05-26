class Calculator:
    def __init__(self):
        self.num = ""
        self.stack = []
        self.operator = ""
        self.subtractFlag = False
        self.decimalFlag = False

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
    
    def add_to_num(self, value):
        self.num += str(value)
    
    def get_num_string(self):
        return self.num

    def return_num(self):
        if not self.num:
            return 0
        if self.subtractFlag:
            return float(self.num) * -1
        return float(self.num)
            
    def clear_num(self):
        self.stack.append(self.return_num())
        self.num = ""
    
    def clear_stack(self):
        self.stack.clear()
    
    def set_operator(self, operator):
        self.operator = operator
        self.clear_num()
        self.set_subtract_flag(False)
        self.set_decimal_flag(False)
    
    def clear_function(self):
        self.clear_num()
        self.clear_stack()
        self.subtractFlag = False
        self.decimalFlag = False
        self.operator = ""


    def calculate(self):
        if not self.stack or not self.num:
            return None
        
        num1 = self.stack.pop()
        num2 = self.return_num()
        
        if self.operator == "+":
            result = self.add(num1, num2)
        elif self.operator == "-":
            result = self.subtract(num1, num2)
        elif self.operator == "x":
            result = self.multiply(num1, num2)
        elif self.operator == "÷":
            result = self.divide(num1, num2)
        elif self.operator == "^":
            result = self.power(num1, num2)
        elif self.operator == "√":
            result = self.square_root(num2)
        elif self.operator == "%":
            result = self.modulus(num1, num2)
        else:
            raise ValueError("Unknown operator")
        
        self.clear_num()
        return result
    
    def get_subtract_flag(self):
        return self.subtractFlag

    def set_subtract_flag(self, bool):
        self.subtractFlag = bool
    
    def get_decimal_flag(self):
        return self.decimalFlag

    def set_decimal_flag(self, bool):
        self.decimalFlag = bool