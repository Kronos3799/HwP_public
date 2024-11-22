def myfunc (*args, **kwargs): # Argumente und Keyword-Argumente
    print(len(args))
    for i in args:
        print(f"args - {i}")

    for key, val in kwargs.items():
        print(f"kwargs - {key} : {val}")

myfunc(1, 2, 3, 4, 5, { "d" : 4, "e" : 5}, first = "sdfsdf" , second = "123123")

# Warum? Ich kann variabel viele Argumente und Keyword-Argumente übergeben