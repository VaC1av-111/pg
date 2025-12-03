class Vector:
    def __init__ (self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'vector ({self.x},{self.y})'
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y) 


if __name__ == "__main__":
    v1 = Vector (2,3)
    v2 = Vector (3,4)

    print (v1)
    print (v2)