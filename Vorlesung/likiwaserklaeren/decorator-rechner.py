def decorator(funktion):
    def inner(a, b):
        return 5 * funktion(a, b)
    
    return inner

@decorator
def addition(a, b):
    return a + b

print(addition(3, 4))  # 35 instead of 7