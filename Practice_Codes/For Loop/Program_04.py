x = int(input("Enter x : "))
y = int(input("Enter y : "))
for i in range(x,y+1):
    if (i%2==0):
        print(i," is even")
    else:
        print(i," is odd")