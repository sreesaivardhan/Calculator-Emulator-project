import ctypes

# Load your compiled shared library
calc = ctypes.CDLL('./libcalc.dll')


# Define argument and return types
calc.add.argtypes = [ctypes.c_long, ctypes.c_long]
calc.add.restype = ctypes.c_long

calc.sub.argtypes = [ctypes.c_long, ctypes.c_long]
calc.sub.restype = ctypes.c_long

calc.mul.argtypes = [ctypes.c_long, ctypes.c_long]
calc.mul.restype = ctypes.c_long

calc.div.argtypes = [ctypes.c_long, ctypes.c_long]
calc.div.restype = ctypes.c_long

# Simple calculator
def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Choose operation (+ - * /): ")

    if op == '+':
        print("Result:", calc.add(a, b))
    elif op == '-':
        print("Result:", calc.sub(a, b))
    elif op == '*':
        print("Result:", calc.mul(a, b))
    elif op == '/':
        if b != 0:
            print("Result:", calc.div(a, b))
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid operation!")

calculator()
