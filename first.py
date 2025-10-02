

def sudy_nebo_lichy(cislo):
    if cislo % 2 < 1 :
        print(f"{cislo} je sudá.")
    
    else:
        print(f"{cislo} je lichá.")

if __name__ == "__main__":
    sudy_nebo_lichy(5)
    sudy_nebo_lichy(1000000)
                    
hodnota = input("Zadej číslo:")

hodnota = int(hodnota)

sudy_nebo_lichy(hodnota)