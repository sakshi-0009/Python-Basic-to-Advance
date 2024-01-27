# Value Error :-

def Add(a, b):
    return a+b

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

ans = num1+num2
print("Addition is: ",ans)

# if num1 = 1 and num2 = sakshi --> ValueError: invalid literal for int() with base 10: 'sakshi'