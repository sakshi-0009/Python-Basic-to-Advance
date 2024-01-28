list1 = [1,"Kanha",2,"Rahul",3]

try:
    index1 = int(input("Enter index1 : "))
    print(list1[index1])

    index2 = int(input("Enter index2 : "))
    print(list1[index2])

    add = (list1[index1]+list1[index2])

except ValueError as err:
    print("ValueError Handled")
except IndexError as err:
    print("IndexError Handled")
except TypeError as err:
    print("TypeError Handled")

else:
    print(add)

print("End code")