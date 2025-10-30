class ChybaDeleniNulou(Exception):
    pass



def vydel (citatel, jmenovatel):
    if jmenovatel == 0:
        raise ChybaDeleniNulou("Deleni nulou neni povoleno.")
    return citatel / jmenovatel


    """                #Zkoušení výjimek/chyb
    try:
        vysledek = citatel / jmenovatel
    except ZeroDivisionError:
        return "Chyba: Deleni nulou neni povoleno."
    else:
        return vysledek

    """

if __name__ == "__main__":
    try:
        cislo1 = None
        while cislo1 is None:
            try:
                cislo1 = int(input("Zadejte citatel: "))
            except Exception:
                print("Zadej validni cislo.")

        cislo2 = int(input("Zadejte jmenovatel: "))

        vysledek = vydel(cislo1, cislo2)

        print(vysledek)

    except ChybaDeleniNulou as e:
        print("Pokusil jste se delit nulou.")


    except Exception as e:
        print("Nastala neocekavana chyba.")