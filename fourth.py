def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka["typ"]
    start = figurka["pozice"]
    start_radek, start_sloupec = start
    cilovy_radek, cilovy_sloupec = cilova_pozice

    if not (1 <= cilovy_radek <= 8 and 1 <= cilovy_sloupec <= 8):
        return False  # Cílová pozice je mimo šachovnici
    
    if cilova_pozice == start:
        return False

    if cilova_pozice in obsazene_pozice:
        return False  # Cílová pozice je obsazená jinou figurou

    rozdil_radek = cilovy_radek - start_radek
    rozdil_sloupec = cilovy_sloupec - start_sloupec

   #Typ figurky a její pohyb
    if typ == "pěšec":
        if rozdil_sloupec == 0 and rozdil_radek == 1 and cilova_pozice not in obsazene_pozice: #jedna v před
            return True
        
        if rozdil_sloupec == 0 and rozdil_radek == 2 and start_radek == 1: #dvojkrok
            if (start_radek + 1, start_sloupec) not in obsazene_pozice: #volná pozice mezi startem a cílem
                return True
        return False
    
    if typ == "jezdec":
        if (abs(rozdil_radek), abs(rozdil_sloupec)) in [(2, 1), (1, 2)]:
            return True
        return False
    
    if typ == "věž":
        if rozdil_radek != 0 and rozdil_sloupec != 0:
            return False
        krok_r = 0 if rozdil_radek == 0 else (1 if rozdil_radek > 0 else -1)
        krok_s = 0 if rozdil_sloupec == 0 else (1 if rozdil_sloupec > 0 else -1)
        r, s = start_radek + krok_r, start_sloupec + krok_s
        while (r, s) != (cilovy_radek, cilovy_sloupec):
            if (r, s) in obsazene_pozice:
                return False
            r += krok_r
            s += krok_s
        return True
    
    if typ == "střelec":
        if abs(rozdil_radek) != abs(rozdil_sloupec):
            return False
        krok_r = 1 if rozdil_radek > 0 else -1
        krok_s = 1 if rozdil_sloupec > 0 else -1
        r, s = start_radek + krok_r, start_sloupec + krok_s
        while (r, s) != (cilovy_radek, cilovy_sloupec):
            if (r, s) in obsazene_pozice:
                return False
            r += krok_r
            s += krok_s
        return True
                
    if typ == "dáma":
        # buď po řádku/sloupci nebo diagonálně
        if rozdil_radek == 0 or rozdil_sloupec == 0:
            krok_r = 0 if rozdil_radek == 0 else (1 if rozdil_radek > 0 else -1)
            krok_s = 0 if rozdil_sloupec == 0 else (1 if rozdil_sloupec > 0 else -1)
        elif abs(rozdil_radek) == abs(rozdil_sloupec):
            krok_r = 1 if rozdil_radek > 0 else -1
            krok_s = 1 if rozdil_sloupec > 0 else -1
        else:
            return False
        r, s = start_radek + krok_r, start_sloupec + krok_s
        while (r, s) != (cilovy_radek, cilovy_sloupec):
            if (r, s) in obsazene_pozice:
                return False
            r += krok_r
            s += krok_s
        return True
        
    if typ == "král":
        return max(abs(rozdil_radek), abs(rozdil_sloupec)) == 1


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