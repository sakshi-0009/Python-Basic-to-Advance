''' Sequence data type have 4 types : 1.String, 2.List, 3.Tuple, 4.Range'''

#   1.String

ProgLang1 = 'C'
print(ProgLang1)
print(type(ProgLang1))  #<class 'str'>

ProgLang2 = "Python"
print(ProgLang2)
print(type(ProgLang2))  #<class 'str'>

ProgLang3 = '''Flutter'''
print(ProgLang3)
print(type(ProgLang3))  #<class 'str'>

ProgLang4 = """Java"""
print(ProgLang4)
print(type(ProgLang4))  #<class 'str'>

#   2.List

playerList = [18,"Virat",45.0,7,"MSD",47.50]
print(playerList)
print(type(playerList))     #<class 'list'>

#   3.Tuple

playerList = (18,"Virat",45.0,7,"MSD",47.50)
print(playerList)
print(type(playerList))     #<class 'tuple'>

#   4.range

x = range(41,51)
print(x)        #range(41, 51)
print(type(x))  #<class 'range'>

for i in x:
    print(i)