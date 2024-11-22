def myfunc(*args, **kwargs):
    print(len(args))
    for i in args:
        print(f"args - {i}")
    
    for key, val in kwargs.items():
        print(f"kwargs: {key} {val}")
    
myfunc(1, 2, 3, 4, 5, name="John", age=25)