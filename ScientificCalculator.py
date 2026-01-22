import math
Operators = """ 
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Remainder (%)
- Power (**)
- Square root (sqrt)
- Trigonometric Functions (sin/cos/tan)
- logarithmic functions (log)
- Factorial (!)
- Absolute (abs)
"""
print("Available Operations : ")
print(Operators)
print("Choose any Operation in the form of Symbol:")
print("Example: +  -  *  /  sqrt  sin  log")
oper = input("Enter Operation:")

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
       if b == 0:
           print("Error! Cannot divide by zero.")
           return None
       return a / b

def rem(a,b):
    if b == 0:
        print("Error! Cannot find remainder with zero.")
        return None
    return a % b

def power(a,b):
    return a ** b

def sq_root(n):
    if n < 0:
        print("Error! Invalid Input for Square Root.")
        return None
    return math.sqrt(n)

def trig(func,n):
    try:
        if func == 'sin':
            return math.sin(math.radians(n))  
        elif func == 'cos':
            return math.cos(math.radians(n))
        elif func == 'tan':
            return math.tan(math.radians(n))
        else:
            print("Use sin, cos, or tan.")
            return None
    except Exception:
        print("Invalid input.")
        return None
    
def log_func(n, base_val):
     if n <= 0:
        print("Error! Log input must be positive.")
        return None
     return math.log(n,base_val)

def fact(n):
    if n < 0:
        print("Error! Factorial is not defined for negative numbers.")
        return None
    return math.factorial(n) 
    
def absolute(n):
    return abs(n)

if oper == '+':
    a = float(input("Enter First Number:"))
    b = float(input("Enter Second Number:"))
    print(f"Addition of {a} and {b} is: {add(a,b)}")

elif oper == '-':
    a = float(input("Enter First Number:"))
    b = float(input("Enter Second Number:"))
    print(f"Subtraction of {a} and {b} is: {sub(a,b)}")

elif oper == '*':
    a = float(input("Enter First Number:"))
    b = float(input("Enter Second Number:"))
    print(f"Multiplication of {a} and {b} is: {mult(a,b)}")

elif oper == '/':
    a = float(input("Enter First Number:"))
    b = float(input("Enter Second Number:"))
    result = div(a, b)
    if result is not None:
        print(f"Division of {a} and {b} is: {result}")
    
elif oper == '%':
    a = int(input("Enter First Number:"))
    b = int(input("Enter Second Number:"))
    print(f"Remainder of {a} and {b} is: {rem(a,b)}")
    
elif oper == '**':
    a = float(input("Enter First Number:"))
    b = float(input("Enter Second Number:"))
    print(f"{a} raised to the power {b} is: {power(a,b)}")
 
elif oper == "sqrt":
    n = float(input("Enter number:"))
    print(f"Square Root of {n} is: {sq_root(n)}")

elif oper in ['sin','cos','tan']:
    n = float(input("Enter Number: "))
    print(f"{oper} {n} degree = {trig(oper,n)}")

elif oper == 'log':
    a = float(input("Enter Number: "))
    base = input("Enter base or Enter for natural log: ")
    base_val = math.e if base == '' or base == 'e' else float(base)
    result = log_func(a, base_val)
    if result is not None:
        print(f"log_{base_val}({a}) = {result}")

elif oper == '!':
    n = int(input("Enter Number:"))
    result = fact(n)
    if result is not None:
       print(f"Factorial of {n} is: {result}")

elif oper == 'abs':
    n = float(input("Enter Number:"))
    print(f"Absolute Value of {n} is: {absolute(n)}")

else:
    print("Invalid Operation Selected.")