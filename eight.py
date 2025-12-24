def bin_to_dec(binarni_cislo):
    binarni_cislo = str(binarni_cislo)
   
    binarni_cislo = binarni_cislo[::-1]
    
    vysledek = 0
    mocnina = 1

    
    for znak in binarni_cislo:
        if znak == '1':
            vysledek = vysledek + mocnina
        mocnina = mocnina * 2
           
    return vysledek


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128


if __name__ == "__main__":
    print(bin_to_dec("0"))
    print(bin_to_dec(1))
    print(bin_to_dec("100"))
    print(bin_to_dec(101))
    print(bin_to_dec("010101"))
    print(bin_to_dec(10000000))