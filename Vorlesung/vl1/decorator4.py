import time

def decorator_time(func):
    def inner(*args, **kwargs):
        print("->decorator_time")
        start = time.time()
        val = func(*args, **kwargs)
        end = time.time()
        print(f"<-decorator_time: {end - start}")
        return val
    
    return inner

