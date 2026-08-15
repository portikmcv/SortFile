import re
def add(a,b):
    return a + b

def subtract(a,b):return a - b

def multiply(a,b):return a*b
    

def divide (a,b):return a/b if b != 0 else "Error"
    


while True:
    equation = input("Your equation: (Example: 2 * 3)")
    Rawpart = re.split(r'([\+\-\*\/])',equation)
    parts = [p.strip() for p in Rawpart if p.strip()]

    if len(parts) != 3:
        print("Invalid format! Please input like '2 * 3'")
    try:
        op = str(parts[1])
        num1 = float(parts[0])
        num2 = float(parts[2])
    except ValueError:
        print("Error: Please enter valid numbers.")

    result = None
    if op == '+':
        result = add(num1,num2)
        
    elif op == '-':
        result = subtract(num1,num2)
        
    elif op == '*':
        result = multiply(num1,num2)
        
    elif op == '/':
        result = divide(num1,num2)

    print(f'Your result = {result}\n')
        


