def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka["typ"]
    radek, sloupec = figurka["pozice"]
    radek, sloupec = startovni_pozice
    cilovy_radek, cilovy_sloupec = cilova_pozice

    if not (1 <= cilovy_radek <= 8 and 1 <= cilovy_sloupec <= 8):
        return False  # Cílová pozice je mimo šachovnici

    if cilova_pozice in obsazene_pozice:
        return False  # Cílová pozice je obsazená jinou figurou

rozdil_radek = cilovy_radek - radek
rozdil_sloupec = cilovy_sloupec - sloupec

def volna_cesta(krok_radek, krok_sloupec):
    radek, sloupec = radek + krok_radek, sloupec + krok_sloupec
    while (radek, sloupec) != (cilovy_radek, cilovy_sloupec):
        if (radek, sloupec) in obsazene_pozice:
            return False
        radek += krok_radek
        sloupec += krok_sloupec
    return True

#Typ figurky a její pohyb
if typ == "pěšec":
        if rozdil_radek == 1 and rozdil_sloupec == 0:
            return True
        else:
            return False
        





if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True