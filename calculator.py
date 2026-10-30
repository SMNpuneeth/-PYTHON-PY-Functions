
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print("******Simple Calculator******")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    option = int(input("Enter your choice: "))

    if option == 5:
        print("Exiting...")
        break

    elif option >= 1 and option <= 4:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if option == 1:
            print("Result:", add(a, b))
        elif option == 2:
            print("Result:", sub(a, b))
        elif option == 3:
            print("Result:", mul(a, b))
        elif b != 0:
            print("Result:", div(a, b))
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid choice")