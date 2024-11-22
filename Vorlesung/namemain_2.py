import namemain_1

print(f"called without if in {__name__}, this is : {namemain_1.__name__}")

if __name__ == "__main__":
    print(f"this is : {__name__}")
    print (f"called with if in {__name__}, this is : {namemain_1.__name__}")