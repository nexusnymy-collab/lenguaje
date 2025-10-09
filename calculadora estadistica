import math 
class Calculadora:
    def __init__(self):
        self.datos = []
        self.cantidad = 0
        self.suma = 0

    def media_muestral(self):
        self.cantidad = int(input("Ingrese la cantidad de datos que va a almacenar: "))
        for i in range(self.cantidad):
            numero = float(input(f"Ingrese el dato {i+1}: "))
            self.datos.append(numero)
        self.suma = sum(self.datos)
        media = self.suma / self.cantidad
        return media

    def varianza_muestral(self, media):
        varianza = 0
        for dato in self.datos:
            varianza += (dato - media) ** 2
        varianza = varianza / (self.cantidad - 1)
        return varianza

    def desviacion_estandar(self, varianza):
        desviacion = math.sqrt(varianza)
        return desviacion 

def main():
    aplicar = Calculadora()
    media = aplicar.media_muestral()
    varianza = aplicar.varianza_muestral(media)
    desviacion = aplicar.desviacion_estandar(varianza)

    print(f"La media muestral es: {media}")
    print(f"La varianza muestral es: {varianza}")
    print (f"la desviacion estandar es de : {desviacion}")


if __name__ == "__main__":
    main()



        

    
        
