import math

def statistika(rezim, cisla):
    
    prazdny = False
    pocet_prvku = 0    

    for x in cisla:
        pocet_prvku += 1
    
    if pocet_prvku == 0:
        prazdny = True


    if rezim == "soucet":
        vysledek = 0
        for x in cisla:
            vysledek += x
        return vysledek

    elif rezim == "pocet":
        return pocet_prvku

    elif rezim == "max":
        if prazdny:
            return None
        maximum = cisla[0]
        for x in cisla:
            if x > maximum:
                maximum = x
        return maximum

    elif rezim == "min":
        if prazdny:
            return None
        minimum = cisla[0]
        for x in cisla:
            if x < minimum:
                minimum = x
        return minimum

    elif rezim == "prumer":
        if prazdny:
            return None
        soucet = 0
        for x in cisla:
            soucet += x
        return soucet / pocet_prvku
  


def test_statistika():
    assert statistika("soucet", [1, 2, 3, 4]) == 10
    assert statistika("soucet", [-1, -2, -3]) == -6
    assert statistika("soucet", []) == 0
    assert statistika("pocet", [1, 2, 3]) == 3
    assert statistika("pocet", []) == 0
    assert statistika("max", [1, 9, 3]) == 9
    assert statistika("max", [-10, -2, -30]) == -2
    assert statistika("max", []) is None
    assert statistika("min", [1, 9, 3]) == 1
    assert statistika("min", [-10, -2, -30]) == -30
    assert statistika("min", []) is None
    assert math.isclose(statistika("prumer", [2, 4, 6]), 4.0)
    assert math.isclose(statistika("prumer", [1, 2]), 1.5)
    assert statistika("prumer", []) is None
    assert statistika("neco", [1, 2, 3]) is None


if __name__ == "__main__":
    print(statistika("soucet", [1, 2, 3]))     # 6
    print(statistika("pocet", [1, 2, 3]))     # 3
    print(statistika("max", [1, 9, 3]))       # 9
    print(statistika("min", [1, 9, 3]))       # 1
    print(statistika("prumer", [2, 4, 6]))    # 4.0
    #TESTY FUNGUJÍ