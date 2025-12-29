class persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def presentarse(self):
        print(f"hola soy {self.nombre} y tengo {self.edad} años")

class trabajador:
    def __init__(self,profesion,salario):
        self.profesion=profesion
        self.salario=salario

    def trabajar(self):
        print(f"estoy trabajando como {self.profesion} y gano $ {self.salario} al mes ")

class estudiante:
    def __init__(self,carrera,universidad):
        self.carrera=carrera
        self.universidad=universidad

    def estudiar(self):
        print(f"estudio {self.carrera} en la universidad{self.universidad}")

class personamultirol(persona,trabajador,estudiante):
    def __init__(self,nombre,edad,profesion,salario,carrera,universidad):
        persona.__init__(self,nombre,edad)
        trabajador.__init(self,profesion,salario)
        estudiante.__init__(self,carrera,universidad)

    def mostrar_informacion(self):
        print("=====INFORMACION DE LA PERSONA=====")
        self.presentarse()
        self.trabajar()
        self.estudiar()

def main():
    persona1=personamultirol(
        nombre="juanita",
        edad=25,
        profesion="desarrollador de software",
        salario=2500,
        carrera="ingenieria estadistica e informatica",
        universidad="universidad nacional del altiplano",
        )
    persona1.mostrar_informacion()
if __name__=="__main__":
    main()

