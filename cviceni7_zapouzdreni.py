class ChybnaCastka(Exception):
    pass


class Bankovniucet:
    def __init__(self, jmeno):
        self.jmeno = jmeno 
        self.__zustatek = 0

    def vloz(self, suma):
            if suma <= 0:
                raise ChybnaCastka("Nelze pridat nulu nebo negativ")    
            self.__zustatek += suma

    def vyber(self, suma):
        if suma

    def __str__(self):
        return f'Ucet vlastní {self.jmeno} a je na něm{self.__zustatek}kc'



if __name__ == "__main__":
    ucet = Bankovniucet("alice")
    print(ucet)

    ucet.vloz(100)
    print(ucet)
    
    ucet.vyber(100)
    print(ucet)    