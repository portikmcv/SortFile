import re
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide (a,b):
    if b != 0:
        return a/b
    else:
        return "B cannot be 0"


while True:
    equation = input("Your equation: (Example: 2 * 3)")
    Rawpart = re.split(r'([\+\-\*\/])',equation)
    parts = [p.strip() for p in Rawpart if p.strip()]
    op = str(parts[1])
    num1 = float(parts[0])
    num2 = float(parts[2])
    if op == '+':
        result = add(num1,num2)
        print(f'Your result = {result}')
    elif op == '-':
        result = subtract(num1,num2)
        print(f'Your result = {result}')
    elif op == '*':
        result = multiply(num1,num2)
        print(f'Your result = {result}')
    elif op == '/':
        result = divide(num1,num2)
        print(f'Your result = {result}')


