import math
class Tvar:
    def obsah(self):
        print ("neni definovano")
    
class ABC(Tvar):
    pass


class Ctverec(Tvar):
    def __init__(self, hrana):
        self.hrana = hrana

    def obsah(self):
        return self.hrana * self.hrana

class Kruh(Tvar):
    def __init__(self, polomer):
        self.polomer = polomer

    def obsah(self):
        return math.pi * self.polomer * self.polomer


if __name__ == "__main__":

    obj = Tvar()

    tvary = [Ctverec(2), Ctverec(3), Kruh(2), Kruh(3), Ctverec(1)]

    for tvar in tvary:
        print(tvar.obsah())

    obj1 = Ctverec(2)
    print(obj1.obsah())
    obj2 = Kruh(3)
    print(obj2.obsah())