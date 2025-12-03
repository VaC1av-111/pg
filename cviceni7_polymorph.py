class Osoba:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def __str__(self):
        return f'Osoba: {self.jmeno}'
    
class Student(Osoba):
    def __init__(self, jmeno, rocnik=1):
        super().__init__(jmeno)
        self.rocnik = rocnik

    def __str__(self):
        return f'Student {self.jmeno} studuje {self.rocnik}'
    
    def dalsi_rocnik(self):
        if self.rocnik >= 5:
            raise Exception ("Na konci studia")
        self.rocnik += 1

class Ucitel(Osoba):
    def __init__(self, jmeno, roky_praxe):
        super().__init__(jmeno)
        self.roky_praxe = roky_praxe

    def __str__(self):
        return f'Ucitel {self.jmeno} ma {self.roky_praxe} let praxe'
    
    def pridat_rok(self):
        self.roky_praxe += 1



    if __name__ == "__main__":

        student1 = Student("alice")
        
        print(student1)