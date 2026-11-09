# Write a program to create a Simple Calculator using a switch case and function for every operation.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Result:", add(a, b))
    case 2:
        print("Result:", subtract(a, b))
    case 3:
        print("Result:", multiply(a, b))
    case 4:
        print("Result:", divide(a, b))
    case _:
        print("Invalid choice")