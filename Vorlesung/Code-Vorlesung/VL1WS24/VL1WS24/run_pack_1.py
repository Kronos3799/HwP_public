import pack_1.pack_file_1
from pack_1 import pack_1_var, pack_1_var_2, pack_1_var_3


if __name__ == "__main__":
    print(f"this is: {__name__} and import {pack_1.__name__}")

    print(pack_1_var)
    print(pack_1_var_2)
    print(pack_1_var_3)
    print(pack_1.pack_file_1.pack_1_func_1())
    print(pack_1.pack_file_1.pack_1_func_2())

    
