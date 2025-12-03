import json

class Car:
    def __init__(self, znacka, model, barva):
        self.znacka = znacka
        self.model = model
        self.barva = barva

    def __str__ (self):
        return f'Auto {self.znacka}/{self.model}/{self.barva}'
    
    @classmethod
    def parse(cls, jdata):
        data = json.loads(jdata)
        for value in ('znacka', 'model', 'barva'):
            if value not in data:
                raise InvalidData('Missing {value} in data')
        return cls (data['znacka'], data['model'], data['barva'])




if __name__ == "__main__":
    jdata1 = '("znacka:" "bmw", "model:" "x5", "barva:" "modra")'
    jdata2 = '("znacka:" "toyota", "model:" "corolla", "barva:" "červená")'
    
    


    auto = Car.parse(jdata2)

    print(auto)