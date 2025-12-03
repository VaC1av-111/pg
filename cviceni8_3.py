class ChybnyZustatek(Exception):
    pass

class ucet:
    def __init__(self):
        self.zustatek = 0

    @property
    def zustatek(self):
        return self.__zustatek
    
    @zustatek.setter
    def zustatek(self, hodnota):
        if hodnota < 0: 
            raise ChybnyZustatek(f'Nelze mit zaporny zustatek')
        self.__zustatek = hodnota

if __name__ == "__main__":
    ucet = ucet()