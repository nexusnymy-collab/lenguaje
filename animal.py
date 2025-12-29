class animal: #clase base
    def __init__(self,nombre):
        self.nombre=nombre

        def hacersonido(self):
            pass
class perro(animal): #clase derivada
    def hacersonido(self):
        return "!guau!"

perro=perro("rex")
print("f{perro.nombre}dice{perro.hacersonido()}")
