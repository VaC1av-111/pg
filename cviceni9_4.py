def nejvetsi(seznam_cisel):
    if not seznam_cisel:
        return None
    nejvetsi_cislo = seznam_cisel[0]
    for cislo in seznam_cisel:
        if cislo > nejvetsi_cislo:
            nejvetsi_cislo = cislo
    return nejvetsi_cislo


def test_nejvetsi():
    assert nejvetsi([1,2,3,4,5]) == 5
    assert nejvetsi([100, 10, 5]) == 100
    assert nejvetsi() == None


if __name__ == "__main__":
    seznam_cisel1 = [3, 5, 2, 8, 1]
    print(nejvetsi(seznam_cisel1))

    seznam_cisel2 = [100, 12, 1]
    print(nejvetsi(seznam_cisel2))

    seznam_cisel3 = []
    print(nejvetsi(seznam_cisel3))