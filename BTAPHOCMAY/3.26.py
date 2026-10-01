x = 5
eta = 0.2

def f(x):
    return x**2

def df(x):
    return 2*x

print("Buoc 0:", x, f(x))

for i in range(1, 5):
    x = x - eta * df(x)
    print("Buoc", i, ":", x, f(x))