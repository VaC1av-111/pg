print("Hello World")

def cislo_mensi_nez_3(hodnota):
    if hodnota > 3:
        print(f"Hodnota {hodnota} je větší než 3");

    elif (hodnota < 3):
       print(f"Hodnota {hodnota} je menší než 3");

    else:
       print(f"Hodnota {hodnota} je 3");

    

cislo = input("Zadej číslo:")

cislo = int(cislo)

cislo *=3
   
print(f"Zadane číslo je: {cislo}")

cislo_mensi_nez_3(1)
cislo_mensi_nez_3(cislo)