import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def perimetro(self):
        p = 2 * math.pi * self.radio
        print(f"El perímetro del círculo de radio {self.radio} es {p:.2f}")

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        p = 4 * self.lado
        print(f"El perímetro del cuadrado de lado {self.lado} es {p:.2f}")

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        p = 2 * (self.base + self.altura)
        print(f"El perímetro del rectángulo de {self.base}x{self.altura} es {p:.2f}")

def calcular(objeto):
    objeto.perimetro()

objetos = [
    Circulo(5),
    Cuadrado(4),
    Rectangulo(6, 3)
]

for objeto in objetos:
    calcular(objeto)


