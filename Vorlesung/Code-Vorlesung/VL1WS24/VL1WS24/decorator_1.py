def myfunc(*args, **kwargs):
    print(len(args))
    for i in args:
        print(f"args - {i}")

    for key, val in kwargs.items():
        print(f"kwargs - {key}:{val}")

myfunc(1,2,3,"df",5, {"d": 4, "e": 5}, first="sdfsdf", second = "123123")

