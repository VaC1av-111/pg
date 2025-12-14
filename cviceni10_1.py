# napište funkci filtruj_cisla(typ, cisla), která přijme dva parametry:
# typ – řetězec, který může nabývat hodnot "kladna", "zaporna", "suda", "licha"
# cisla – seznam čísel
# Funkce vrátí nový seznam obsahující pouze ta čísla z parametru cisla, která odpovídají zadanému typu.

def filtruj_cisla(typ, cisla):
    if typ == "kladna":
        vysledek = [x for x in cisla if x > 0]
    elif typ == "zaporna":
        vysledek = [x for x in cisla if x < 0]
    elif typ == "suda":
        vysledek = [x for x in cisla if x % 2 == 0]
    elif typ == "licha":
        vysledek = [x for x in cisla if x % 2 != 0]
    else:
        vysledek = []
    # Vaše řešení zde
 
    return vysledek


if __name__ == "__main__":
    print(filtruj_cisla("kladna", [1, -2, 0, 5, -3]))   # [1, 5]
    print(filtruj_cisla("suda", [1, 2, 3, 4, 5]))       # [2, 4]
    print(filtruj_cisla("zaporna", [1, -2, 0, 5, -3]))   # [-2, -3]
    print(filtruj_cisla("licha", [1, 2, 3, 4, 5]))       # [1, 3, 5]
    # neexistující typ
    print(filtruj_cisla("xxx", [1, 2, 3]))              # []