# Herausfinden ob ein Modul (Codeschnippsel) direkt oder indirekt aufgerufen wird


print(f"called without, if this is {__name__}") # wird ausgegeben, wenn das Modul direkt aufgerufen wird - wird immer ausgegeben

if __name__ == "__main__":
    print(f"call within, if this is {__name__}") # wird ausgegeben, wenn das Modul indirekt aufgerufen wird - wird nur ausgegeben, wenn das Modul main ist