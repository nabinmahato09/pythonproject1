username = "humaurtum"

def func():
    username ="hum"
    print(username)
    
print(username)
func()

x = 56
def func2(y):
    z = x + y
    return z
result = func2(1)
print(result)

def f1():
    x = 99
    def f2():
        print(x)
    f2()
f1()