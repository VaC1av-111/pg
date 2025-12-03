class Banka:
    def __init__(self, nazev):
        self.nazev = nazev

    def zaloz_ucet(self, osoba):
        novy_ucet = Ucet(osoba)
        osoba.prirad_ucet(novy_ucet)
        self.ucty.append(novy_ucet)


class Osoba:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.ucet = None


    def prirad_ucet(self, ucet):
        self.ucet = ucet


class Ucet:
    def __init__(self, majitel):
        self.majitel = majitel

    def zustatek(self, zustatek):
        return zustatek
    
    def vloz(self, castka):
        if castka <= 0:
            raise Exception("Zaporna castka")
        self.zustatek += castka

    def vyber(self, castka):
        if castka <= 0:
            raise Exception("Zaporna castka")
        self.zustatek += castka

    def __str__(self):
        return f'Ucet({self.majitel.jmeno}): {self.zustatek}'

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    osoba1 = Osoba("BOB")
    osoba2 = Osoba("Alice")

    banka1 = Banka("KB")
    banka1.zaloz_ucet(osoba1)