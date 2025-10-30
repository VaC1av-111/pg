def precti_hodnoty_a_incrementuj(file):
    
    for line in file:
         

if __name__ == "__main__":

    try:
        name = input("Zadejte jemno souboru: ")
        file = open (name, 'r')

        precti_hodnoty_a_incrementuj(file)

    except FileNotFoundError:
        print("Soubor nebyl nalezen.")

    