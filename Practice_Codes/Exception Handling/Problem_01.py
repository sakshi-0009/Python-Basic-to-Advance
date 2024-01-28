print("Start code")

try:
    num1 = int(input("Enter num1 : "))
except ValueError as err:
    print("Please enter valid integer number")
    num1 = int(input("Enter num1 : "))

try:
    num2 = int(input("Enter num2 : "))
except ValueError as err:
    print("Please enter valid integer number")
    num2 = int(input("Enter num2 : "))

try:
    print(num1+num2)
except TypeError as err:
    print("Exception handled 3")

print("End code")