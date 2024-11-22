import time

def addition(x, y):
    print(f"<> addition {x}, {y}")
    return x + y

def subtraction(x, y):
    print(f"<> subtraction {x}, {y}")
    return x + y

def decorator_print(func):
    def inner (*args, **kwargs):
        print("->decorator_print")
        val = func(*args, **kwargs)
        print("<-decorator_print")
        return val
    
    return inner

def decorator_time(func):
    def inner (*args, **kwargs):
        print("->decorator_time")
        start = time.time()
        val = func(*args, **kwargs)
        end = time.time()
        print(f"<-decorator_time: {end - start}")
        return val
    
    return inner

theAdd1 = decorator_time(addition)
theAdd = decorator_print(theAdd1)

theSub1 = decorator_time(subtraction)
theSub = decorator_print(theSub1)

print(theAdd(3, 6))
print(theSub(3, 3))