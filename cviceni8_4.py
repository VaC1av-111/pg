class InvalidData(Exception):
    pass


class Osoba:
    def __init__(self, jmeno, telefon, mail):
        self.jmeno = jmeno
        self.telefon = telefon
        self.mail = mail

    def __str__(self):
        return f'Osoba {self.jmeno}, {self.telefon}, {self.mail}'
    
    @property
    def jmeno(self):
        return self.__jmeno
    
    @jmeno.setter
    def jmeno(self, hodnota: str):
        for c in hodnota:
            if not c.isalpha() and not c.isspace():
                raise InvalidData(f'Chyba ve jmene "{hodnota}"')
        self.__jmeno = hodnota
       
    @property
    def telefon(self):
        return self.__telefon
    
    @jmeno.setter
    def telefon(self, hodnota: str):
        if not len(hodnota) == 13:
                raise InvalidData(f'Cislo musi mit 13 znaku')
        if hodnota [0] != "+":
                raise InvalidData(f'Musi mit +')
        if not hodnota [1:].isdigit():
                raise InvalidData(f'neni cislo')
        self.__telefon = hodnota
    
    @property
    def mail(self):
        return self.__mail
    
    @mail.setter
    def mail(self, hodnota: str):
        if '@' not in hodnota:
             raise InvalidData(f'Musi mit @')
        if not hodnota.endswith('.cz'):
             raise InvalidData(f'Musi mit koncovku')
        if not hodnota.replace('@','').replace('',''):
             None
        self.__jmeno = hodnota

    if __name__ == "__main__":
        
        #o1 = Osoba("12345", "+420823123456", "pepek@bbo.net")
    
       # print(o1)
        pass