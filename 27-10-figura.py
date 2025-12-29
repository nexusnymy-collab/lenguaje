class figura:
    def area(self):
        pass

class cuadrado(figura):
    def __init__(self,lado):
        self.lado=lado

    def area(area):
        return self.lado**2

class circulo(figura):
    def __init__(self,radio):
        self.radio=radio

    def area(self):
        return maph.pi*(self.radio**2)

class triangulo(figura):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area(self):
        return (self.base*self.altura)/2

figura=[cuadrado(4),circulo(3),triangulo(5,2)]
for figura in figura:
    print(f"area:{figura.area()}")
