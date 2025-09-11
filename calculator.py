print("Första nummret")
num1 = input()
print("Andra nummret")
num2 = input()

num1 = int(num1)
num2 = int(num2)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Välj operation")
print("1. Addition")
print("2. Minus")
print("3. Multi")
print("4. Dela")

choice = input()

if choice == "1":
    result = add(num1, num2)
    print("Svaret är", result)

elif choice == "2":
    result = subtract(num1, num2)
    print("Svaret är", result)

elif choice == "3":
    result = multiply(num1, num2)
    print("Svaret är", result)

elif choice == "4":
    result = divide(num1, num2)
    print("Svaret är", result)

else:
    print("Fel")