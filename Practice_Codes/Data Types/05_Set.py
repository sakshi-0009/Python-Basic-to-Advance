setData = {10,20,30,40,50}
print(setData)
print(type(setData))    #<class 'set'>

setData[3] = 45         #TypeError: 'set' object does not support item assignment
print(setData)