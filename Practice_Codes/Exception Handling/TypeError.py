# Type Error :-

# eg.1 :-
def fun(a, b):
    print(a)
    print(b)

print("Start code")
fun(10,20)
# fun(10)     TypeError: fun() takes 0 positional arguments but 2 were given
print("End code")

# eg.2 :-
def fun(a, b):
    return a+b

print("Start code")
fun(10,20)
# fun(10,"Sakshi")      TypeError: unsupported operand type(s) for +: 'int' and 'str'
print("End code")