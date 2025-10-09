if __name__ == "__main__":

    def cislo_text(cislo):
        jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
        desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
        teen = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
        stovky = ["", "sto", "dvě stě", "tři sta", "čtyři sta", "pět set", "šest set", "sedm set", "osm set", "devět set"]

       
        cislo = int(cislo)

        if cislo == 0:
            return jednotky[0]          #FUNGUJE, zobrazí nula
        
        if cislo < 10:
            return jednotky[cislo]      #FUNGUJE, zobrazí čísla 1-9
        
        if cislo < 20:
            return teen[cislo % 10]     #FUNGUJE, zobrazí čísla 10-19
        
        if cislo <= 99:                 #FUNGUJE, zobrazí čísla 20-99
            if cislo%10 == 0:
                return stovky[cislo // 100] + " " + desitky[(cislo % 100) // 10]
            else:
                return stovky[cislo // 100] + " " + desitky[(cislo % 100) // 10] + " " + jednotky[cislo % 10]
            
        if cislo >= 100:                #FUNGUJE, zobrazí čísla 100-999
            if cislo % 100 == 0:
                return stovky[cislo // 100]                       
            elif cislo % 100 < 10:
                return stovky[cislo // 100] + " " + jednotky[cislo % 10] 
            elif cislo % 100 < 20:
                return stovky[cislo // 100] + " " + teen[cislo % 10]       
            elif cislo % 10 == 0:
                return stovky[cislo // 100] + " " + desitky[(cislo % 100) // 10]  
            else:
                return (stovky[cislo // 100] + " " + desitky[(cislo % 100) // 10] + " " + jednotky[cislo % 10])                              # např. 256 → "dvě stě padesát šest"



    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)