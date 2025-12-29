class narrador: #clase base
    def nadar(self):
        print("nadando en el agua")

class volador: #clase base 2
    def volar(self):
        print("volando por el aire")

class pato(narrador,volador): #clase derivada
    def graznar(self):
        print("¡cuac!")

pato=pato()
pato.nadar()
pato.volar()
pato.graznar()
