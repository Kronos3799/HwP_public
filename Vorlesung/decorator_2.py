def addition(x, y):
    print(f"<> addition {x}, {y}")
    return x + y

def subtraction(x, y):
    print(f"<> subtraction {x}, {y}")
    return x + y

def func(x, y, func):
    return func(x, y)

print(func(x = 3, y = 4, func = addition))
print(func(x = 5, y = 2, func = subtraction))