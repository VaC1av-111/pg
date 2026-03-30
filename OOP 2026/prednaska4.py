from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: int = 1000
    tags: list = field(default_list=list)

class Product2:
    def __init__ (self, name, price = 1000, tags = []):
        self.name = name
        self.price = price
        self.tags = tags

    def __repr__(self):
        return f"Products2: name=(self.name), price=(self.price), tags=(self.tags)"
    

if __name__ == "__main__":
    p1 = Product2 ("Zubní kartaček")
    print (p1 )
    p2 = Product2("Pasta")