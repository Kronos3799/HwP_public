def addition(x,y):
    print(f"<>addition({x},{y})")
    return x+y


def subtraction(x,y):
    print(f"<>subtraction({x},{y})")
    return x-y


def func(x,y,func):
    return func(x,y)

print(func(3,4, addition))
print(func(5,2, subtraction))
