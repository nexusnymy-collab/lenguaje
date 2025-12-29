class circulo:
    def formar(self):
        print("")

class cuadrado:
    def mover(self):
        print("el pez nada")

class rectangulo:
    def mover(self):
        print("la persona camina")

def desplazar(objeto):
    objeto.mover()

objeto=[pajaro(),pez(),persona()]

for objeto in objeto:
    desplazar(objeto)
