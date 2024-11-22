import time

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

@decorator_print
@decorator_time
def addition(x, y):
    print(f"<> addition {x}, {y}")
    return x + y

@decorator_print
@decorator_time
def subtraction(x, y):
    print(f"<> subtraction {x}, {y}")
    return x + y

print(addition(x = 3, y = 3))
print(subtraction(x = 2, y = 3))