def addition(a, b):
    print("<>addition({x}, {y})")
    return a + b

def subtraction(a, b):
    print("<>subtraction({x}, {y})")
    return a - b

def func(x, y, func):
    return func(x, y)

print(func(x=10, y=5, func=addition))

print(func(10, 5, subtraction))