import namemain1

print(f"called without if in {__name__}, this is {namemain1.__name__}")

if __name__ == "__main__":
    print(f"Hello, {__name__}!")