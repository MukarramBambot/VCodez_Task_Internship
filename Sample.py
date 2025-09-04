# Subtraction: no argument, no return
def subtraction():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Subtraction Result:", a - b)

# Call the function
subtraction()

print("************************************************************************************************")

# Multiplication: with argument, no return
def multiplication(x, y):
    print("Multiplication Result:", x * y)

# Call the function
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
multiplication(num1, num2)

print("************************************************************************************************")

# Division: no argument, with return
def division():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a / b

# Call the function
result = division()
print("Division Result:", result)

print("************************************************************************************************")

# Modulus: with argument, with return
def modulus(x, y):
    return x % y

# Call the function
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = modulus(num1, num2)
print("Modulus Result:", result)
