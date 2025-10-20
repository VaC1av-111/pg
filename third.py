def je_prvocislo(cislo):            # Vrátí True, pokud je n prvočíslo, jinak False.
    if cislo <= 1:              #Vypouští 1 a méně
        return False
    if cislo == 2:          
        return True
    if cislo % 2 == 0:
        return False
    for i in range(3, int(cislo ** 0.5) + 1, 2):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    return [i for i in range(2, maximum + 1) if je_prvocislo(i)]

if __name__ == "__main__":
    cislo = int(input("Zadej cislo: "))         #Input pro číslo
    maximum = int (input("Zadej maximum: "))    #Input pro maximum
    print(vrat_prvocisla(maximum))              #Vypíše číslo do maxima
    print(je_prvocislo(cislo))                  #Vypíše jestli je číslo prvočíslo True/False



    print("Testy:")
    print(je_prvocislo(1))      #False
    print(je_prvocislo(2))      #True
    print(je_prvocislo(3))      #True
    print(je_prvocislo(100))    #False
    print(je_prvocislo(101))    #True

    print(vrat_prvocisla(1))    #[]
    print(vrat_prvocisla(2))    #[2]
    print(vrat_prvocisla(3))    #[2, 3]
    print(vrat_prvocisla(10))   #[2, 3, 5, 7]