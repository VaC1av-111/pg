from abc import ABC, abstractclassmethod
import math

class Tvar:
    def spocitej_obsah(self):
        return None
    

class Obdelnik(Tvar):
    def __init__(self, sirka, delka):
        self.sirka = sirka
        self.delka = delka

    def spocitej_obsah(self):
        return self.sirka * self.delka
    
class Kruh (Tvar):
    def __init__(self, polomer):
        self.polomer = polomer

    def spocitej_obsah(self):
        return math.pi * self.polomer * self.polomer
    
if __name__ == "__main__":

    obj = Kruh(5)
    print (obj)
        