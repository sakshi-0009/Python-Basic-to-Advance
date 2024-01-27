def Div(x, y):
    return x//y

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

ans = Div(num1,num2)
print("Addition is: ",ans)

# if num1 = 145 and num2 = 0 --> ZeroDivisionError: integer division or modulo by zero