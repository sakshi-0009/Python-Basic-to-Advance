listData = [10,20,30,40,50]
byteData = bytes(listData)
print(listData)
print(byteData)     #b'\n\x14\x1e(2'

for i in byteData:
    print(i)        #10 20 30 40 50