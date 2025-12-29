class figurageometrica:
    def __init__(self,nombre):
        self.nombre=nombre

    def area(self):
        raise NotImplementedError("subclase deben implementar este metodo")

    def perimetro(self):
        raise NotImplementedError("subclase deben implementar este metodo")


class circulo(figurageometrica):
    def __init__(self,radio):
        super().__init__("circulo")
        self.radio=radio

    def area(self):
        return 3.141592*(self.radio**2)
    
    def perimetro(self):
        return 2*3.141592*self.radio

circulo=circulo(5)
print(f"nombre:{circulo.nombre}")
print(f"area:{circulo.area}")
print(f"perimetro:{circulo.perimetro():.2f}")

    
    
