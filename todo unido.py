class Clasificador:
    def __init__(self):
        self.total = 0

    def clasificar_num(self):
        print("Clasifica números como par, impar o nulo y calcula la suma.")
        print("Escribe números para analizar. Escribe 'fin' para terminar.")

        entrada = " "
        while entrada.lower() != "fin":
            entrada = input("Ingrese un número: ")

            if entrada.isdigit():
                numero = int(entrada)
                self.total += numero

                if numero == 0:
                    print(f"{numero} es nulo")
                elif numero % 2 == 0:
                    print(f"{numero} es par")
                else:
                    print(f"{numero} es impar")

            elif entrada.lower() != "fin":
                print("Entrada inválida. Ingrese un número o 'fin'.")

        print(f"\nLa suma total es: {self.total}")


def main():
    calculadora = Clasificador()
    calculadora.clasificar_num()


if __name__ == "__main__":
    main()

#par o impar
class IP:
    def __init__(self,limite):
        self.limite = limite
    def clasificar(self):
        for i in range(0,self.limite+1):
            if i==0:
                print(f"{i}-nulo")
            elif i%2==0:
                print(f"{i}-par")
            else:
                print(f"{i}-impar")
    

def main():
    miclasificacion=IP(10)
    resultado=miclasificacion.clasificar()
    

if __name__ == "__main__":
    main()

class Numero:
    def __init__(self,cantidad):
        self.cantidad = cantidad
        self.contador = 0
    def generar_serie(self):
        print("numeros con while")
        while self.contador<self.cantidad:
            print (self.contador,end=" ")

            self.contador+=1

def main():
    minumero=Numero(10)
    minumero.generar_serie()
if __name__=="__main__":
    main()

class Verificador:
    def __init__(self):
        self.entrada = ""

    def verificar(self):
        print("Programa que verifica si un número está entre 1 y 10")
        print("Escribe un número o 'fin' para terminar")

        while self.entrada.lower() != "fin":
            self.entrada = input("Ingrese un número: ")

            if self.entrada.lower() == "fin":
                break

            if self.entrada.isdigit():
                numero = int(self.entrada)
                if 1 <= numero <= 10:
                    print(f"{numero} está entre 1 y 10")
                else:
                    print(f"{numero} no está entre 1 y 10")
            else:
                print("Entrada inválida, ingrese un número o 'fin'.")

        print("Programa finalizado.")


def main():
    verificador = Verificador()
    verificador.verificar()


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox

class Tabla:
    def __init__(self, numero):
        self.numero = numero

    def multiplicar(self):
        resultado = []
        for i in range(1, 11):
            operacion = f"{self.numero} x {i} = {self.numero * i}"
            resultado.append(operacion)
        return resultado


def generar_tabla():
    try:
        numero = int(entry.get())  # tomar número del cuadro de texto
        mitabla = Tabla(numero)
        resultadof = mitabla.multiplicar()

        # Limpiar el texto anterior
        text_area.delete("1.0", tk.END)

        # Mostrar la tabla
        for linea in resultadof:
            text_area.insert(tk.END, linea + "\n")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número entero válido.")


# Ventana principal
root = tk.Tk()
root.title("Tabla de Multiplicar")

# Entrada de número
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label = tk.Label(frame, text="Ingrese un número:")
label.pack(side="left")

entry = tk.Entry(frame, width=10)
entry.pack(side="left", padx=5)

btn = tk.Button(frame, text="Generar", command=generar_tabla)
btn.pack(side="left")

# Área de texto para mostrar la tabla
text_area = tk.Text(root, width=30, height=12, fg="blue")
text_area.pack(pady=10)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

class CL:
    def __init__(self, longitud, altura, ancho, JV, JH):
        self.longitud = longitud
        self.altura = altura
        self.ancho = ancho
        self.JV = JV
        self.JH = JH

    def calcular_CL(self):
        return 1 / ((self.longitud + self.JH) * (self.altura + self.JV))


def calcular():
    try:
        # Obtener valores desde las entradas
        longitud = float(entry_longitud.get())
        altura = float(entry_altura.get())
        ancho = float(entry_ancho.get())
        JV = 0.015
        JH = 0.015

        # Crear objeto y calcular
        operacion = CL(longitud, altura, ancho, JV, JH)
        cl = operacion.calcular_CL()

        # Resultados
        resultado1 = f"La cantidad de ladrillos en un m² es de: {cl:.2f}"
        resultado2 = f"El valor total por m² es de: {cl*1.05:.2f}"
        resultado3 = f"La cantidad total en un área de 8.05 m² es: {cl*8.05*1.05:.2f}"

        # Mostrar en el cuadro de texto
        text_resultados.delete("1.0", tk.END)
        text_resultados.insert(tk.END, resultado1 + "\n")
        text_resultados.insert(tk.END, resultado2 + "\n")
        text_resultados.insert(tk.END, resultado3 + "\n")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")


# Crear ventana
ventana = tk.Tk()
ventana.title("Cálculo de Ladrillos")
ventana.geometry("400x350")

# Etiquetas y entradas
tk.Label(ventana, text="Longitud del ladrillo (m):").pack(pady=5)
entry_longitud = tk.Entry(ventana)
entry_longitud.pack()

tk.Label(ventana, text="Altura del ladrillo (m):").pack(pady=5)
entry_altura = tk.Entry(ventana)
entry_altura.pack()

tk.Label(ventana, text="Ancho del ladrillo (m):").pack(pady=5)
entry_ancho = tk.Entry(ventana)
entry_ancho.pack()

# Botón para calcular
btn_calcular = tk.Button(ventana, text="Calcular", command=calcular)
btn_calcular.pack(pady=10)

# Caja de resultados
text_resultados = tk.Text(ventana, height=6, width=45)
text_resultados.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()

class Fibonacci:
    def __init__(self,cantidad):
        self.cantidad = cantidad
        self.serie=[]
    def generar_serie(self):
        a,b = 0,1
        for _ in range (self.cantidad):
            self.serie.append(a)
            a,b=b,a+b
        return self.serie

def main():
    cantidad = float(input("ingrese la cantidad de numeros fibonacci a imprimir:"))
    mifibonacci = Fibonacci(cantidad)
    resultado = mifibonacci.generar_serie()
    print(resultado)
if __name__=="__main__":
    main()

class Fibonacci:
    def __init__(self,cantidad):
        self.cantidad = cantidad
        self.a = 0
        self.b = 1
        self.contador = 0
    def generar_serie(self):
        print("serie de Fibonacci")
        while self.contador<self.cantidad:
            print (self.a,end=" ")
            c= self.a+self.b
            self.a=self.b
            self.b=c
            self.contador+=1

def main():
    mifibonacci=Fibonacci(10)
    mifibonacci.generar_serie()
if __name__=="__main__":
    main()

class factorial:
    def __init__(self, numero):
        self.numero = numero
        self.resultado = 1
    def calcular(self):
        if self.numero < 0:
            print ("El fatorial no esta definido para numeros negativos")
            return None
        for i in range(1,self.numero+1):
            self.resultado*= i
        return self.resultado
def main():
    mifactorial = factorial(5)
    resultado=mifactorial.calcular()
    if resultado is not None:
        print (f"El factorial de {mifactorial.numero} es {resultado}")
if __name__=="__main__":
    main()

               
    

import gc

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        print(f"Estudiante registrado: {self.nombre}, {self.edad} años, {self.carrera}")

    def mostrar_informacion(self):
        print(f"{self.nombre} estudia {self.carrera} y tiene {self.edad} años")

    def __del__(self):
        print(f"Estudiante eliminado: {self.nombre}")



datos_estudiantes = [
    ("Ana", 20, "Medicina"),
    ("Luis", 22, "Ingeniería"),
    ("Carla", 19, "Arquitectura")
]

grupo = []


for datos in datos_estudiantes:
    estudiante = Estudiante(*datos)
    estudiante.mostrar_informacion()
    grupo.append(estudiante)
grupo.clear()
del estudiante
gc.collect()
print("fin del prohrama")

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre #atributo privado
        self.__edad = edad #atributo privado
    def get_edad(self):
        return self.__edad
    def get_nombre(self):
        return self.__nombre
    def set_edad(self,nueva_edad):
    
        if nueva_edad > 0:
            self.__edad=nueva_edad
        else:
            print("Edadno valida")
    def set_nombre(self,nuevo_nombre):
    
            self.__nombre=nuevo_nombre
            
persona = Persona("Ana",30)
print(persona.get_nombre())
print(persona.get_nombre(),persona.get_edad())
persona.set_edad(35)
persona.set_nombre("Maria")
print(persona.get_nombre(),persona.get_edad())

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre #atributo privado
        self.__edad = edad #atributo privado
    def get_edad(self):
        return self.__edad
    def get_nombre(self):
        return self.__nombre
    def set_edad(self,nueva_edad):
    
        if nueva_edad > 0:
            self.__edad=nueva_edad
            
        else:
            print("Edadno valida")
    def set_nombre(self,nuevo_nombre):
    
            self.__nombre=nuevo_nombre
            
persona = Persona("Ana",30)
print(persona.get_nombre())
print(persona.get_nombre(),persona.get_edad())
persona.set_edad(35)
persona.set_nombre("Maria")
print(persona.get_nombre(),persona.get_edad())

Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
=========== RESTART: C:\Nueva carpeta\programas\signos zodiacales.py ===========
=== Calculadora de Signo Zodiacal ===
Ingresa tu día de nacimiento (1-31): 19
Ingresa tu mes de nacimiento (1-12): 3
Tu signo zodiacal es: Piscis
>>> 

import gc

class Curso:
    def __init__(self, nombre,codigo,profesor):
        self.nombre = nombre
        self.codigo=codigo 
        self.profesor=profesor
        print(f"\nCurso registrado: {self.nombre} - {self.codigo} con el docente {self.profesor}")

    def mostrar_informacion(self):
        print(f"{self.nombre} con el codigo {self.codigo} a cargo del docente {self.profesor}")

    def __del__(self):
        print(f"Curso eliminado: {self.nombre}")

curso_datos = [
    ("LP2", "EST204","Coyla Idme Leonel" ),
    ("Programacion Numerica","EST305", "torres Crux Fred"),
    ("Base de datos", "EST5049678349520","Milan")
]

wa = []


for datos in curso_datos:
    sas = Curso(*datos)
    sas.mostrar_informacion()
    wa.append(sas)




wa.clear()   
del sas
gc.collect()         

print("Fin del programa")

import math

class TR:
    def __init__(self, catetoA, catetoB):  # constructor
        self.catetoA = catetoA
        self.catetoB = catetoB

    def calH(self):
        hipotenusa = math.sqrt(self.catetoA**2 + self.catetoB**2)
        return hipotenusa

    def __del__(self):
        print("Objeto TR destruido")

def main():
    try:
        cateto1 = float(input("Ingrese el valor del primer cateto: "))
        cateto2 = float(input("Ingrese el valor del segundo cateto: "))

        triangulo = TR(cateto1, cateto2)
        resultado = triangulo.calH()

        print(f"La hipotenusa del triángulo con los catetos {triangulo.catetoA} y {triangulo.catetoB} es {resultado:.2f}")

    except NameError:
        print("el objeto ha sido eliminado")
if __name__ == "__main__":
    main()

class Motor:
    def __init__(self,tipo):
        self.tipo = tipo
    def encender(self):
        print(f"Motor : {self.tipo} encendido")
class Auto:
    def __init__(self,marca):
        self.marca = marca
        self.motor = Motor("Electrico")
    def arrancar(self):
        print(f"Auto : {self.marca} arrancando")
        self.motor.encender()
Miauto=Auto("Tesla")
Miauto2=Auto("Toyota")
Miauto.arrancar()
Miauto2.arrancar()

import math
class comida:
    def __init__(self,proteinas,carbohidratos,grasas):
        self.proteinas=proteinas
        self.carbohidratos=carbohidratos
        self.grasas=grasas
        print("objeto comida creado")
        print(f"proteinas,{self.proteinas}.g-carbohidratos,{self.carbohidratos}.g-grasas,{self.grasas}.g")
    def calC(self):
        calorias= self.proteinas*4+self.carbohidratos*4+self.grasas*9
        return calorias
    def mostrarI(self):
        print("informacion nutricional")
        print(f"proteinas-{self.proteinas}.g")
        print(f"carbohidratos-{self.carbohidratos}.g")
        print(f"grasas-{self.grasas}.g")
        print(f"calorias totales-{self.calC()}.kcal")
desayuno=comida(30,50,20)
desayuno.mostrarI()
almuerzo=comida(4,5,6)
almuerzo.mostrarI()
cena=comida(7,8,9)
cena.mostrarI()
del desayuno

try:
    print(desayuno)
except NameError:
    print("el objeto desyuno ha sido eliminado1")
almuerzo.mostrarI()
desayuno.mostrarI()


class Coche:
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def mostrar_info(self):
        print(f"Coche:{self.marca} {self.modelo} {self.color}")
        
    def arrancar(self):
        print(f"Coche {self.marca} {self.modelo} {self.color} ha arrancado")
        
marca = input("ingrese la marca del coche:")
modelo = input("ingrese el modelo del coche:")
color = input("ingrese el color del coche:")

#crear un obleto

mi_coche = Coche(marca,modelo,color)

#usar metodos del objeto


mi_coche.mostrar_info()
mi_coche.arrancar()



#clase numero
#atributo valor
#accion clasifircar
#objeto par impar nulo  
class numero:
    
    def __init__(self,valor):
        self.valor = valor
    
    def clasificar(self):
        if self.valor == 0:
            return "Nulo"
        elif self.valor % 2 ==0:
            return "Par"
        else:
            return "impar"
ejemplos = [numero(0), numero(2), numero(5)]

for num in ejemplos:
    tipo = num.clasificar()
    print(f"el  numero {num.valor} es {tipo}")

import math
class circulo:
    def __init__(self,radio):
        self.radio=radio
    def calA(self):
        area=math.pi*self.radio**2
        return area



rad=float(input("ingrese el radio del circulo"))

circul=circulo(rad)
resultado=circul.calA()

print(f"el area del circulo es {resultado} ")

del circul

try:
    #circulo.calcular_area()
    print(circul)
except NameError:
    print("el objeto ha suido eliminado")

import math
class Circulo:
    def __init__(self,radio):
        self.__radio=radio
    
    
    def get_radio(self):
        return slef._radio
    def set_radio(self,nuevo_radio):
        if nuevo_radio > 0:
            self.__radio=nuevo_radio
        else:
            print("radio no  valida")
    def area(self):
        return math.pi*self.__radio**2
    def perimetro(self):
        return 2*math.pi*self.__radio
    
    
circulo = Circulo(5)

print("area del circulo es:", round (circulo.area(),2))
print("perimetro del circulo es:",round (circulo.perimetro(),2))



class Estadistica:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.datos = []

    def ingresar_datos(self):
        print(f"Ingrese {self.cantidad} datos numéricos:")
        for i in range(self.cantidad):
            valor = float(input(f"Dato {i+1}: "))
            self.datos.append(valor)

    def calcular_media(self):
        suma = 0
        for x in self.datos:
            suma = suma + x
        return suma / self.cantidad

    def calcular_varianza(self, media):
        suma_cuadrados = 0
        for x in self.datos:
            suma_cuadrados = suma_cuadrados + (x - media) ** 2
        return suma_cuadrados / self.cantidad

    def calcular_raiz(self, numero):
        # Método de Newton para la raíz cuadrada
        aproximacion = numero
        for _ in range(20):
            aproximacion = 0.5 * (aproximacion + numero / aproximacion)
        return aproximacion

    def mostrar_resultados(self):
        media = self.calcular_media()
        varianza = self.calcular_varianza(media)
        desviacion = self.calcular_raiz(varianza)

        print("\nResultados:")
        print(f"Media: {media:.2f}")
        print(f"Varianza: {varianza:.2f}")
        print(f"Desviación Estándar: {desviacion:.2f}")


def main():
    mi_estadistica = Estadistica(20)
    mi_estadistica.ingresar_datos()
    mi_estadistica.mostrar_resultados()

if __name__ == "__main__":
    main()

class calculadora:
    def __init__ (self,a,b):
        self.__a=a
        self.__b=b
    def get_a(self):
        return self.__a
    def set_a(self,nuevo_a):
        if nuevo_a > 0:
            self.__a=nuevo_a
        else:
            print("numero no valida")
    def get_b(self):
        return self.__b
    def set_b(self,nuevo_b):
        if nuevo_b > 0:
            self.__b=nuevo_b
        else:
            print("numero no valida")
    def suma(self):
        return self.__a+self.__b
    def resta(self):
        return self.__a-self.__b
    def mult(self):
        return self.__a*self.__b
    def div(self):
        return self.__a/self.__b
cal=calculadora(2,5)

print("la suma de los numeros es:", int(cal.suma()))
print("la resta de los numeros es:", int(cal.resta()))
print("la multiplicacion de los numeros es:", float(cal.mult()))
print("la division de los numeros es:", float(cal.div()))
cal.set_a(8)
print("la suma de los numeros es:", int(cal.suma()))
print("la resta de los numeros es:", int(cal.resta()))
print("la multiplicacion de los numeros es:", float(cal.mult()))
print("la division de los numeros es:", float(cal.div()))

class CL:
    def __init__(self,longitud,altura,ancho,JV,JH):
        self.longitud = longitud
        self.altura = altura
        self.ancho = ancho
        self.JV = JV
        self.JH = JH

    def calcular_CL(self):
        return 1/((self.longitud+JH)*(self.altura+JV))


longitud = float(input("ingrese la longitud del ladrillo:"))
altura = float(input("ingrese la altura del ladrillo:"))
ancho = float(input("ingrese el ancho del ladrillo:"))
JV = 0.015
JH = 0.015

operacion = CL(longitud,altura,ancho,JV,JH)

print ("la cantidad de ladrillos en un metro cuadrado es de:", operacion.calcular_CL()  )
print ("el valor total es de:", operacion.calcular_CL()*1.05,"por metro cuadrado.")
print ("La cantidad total de ladrillos en un area de 8.05 es de:", operacion.calcular_CL()*8.05*1.05)

import gc
class Libro:
    def __init__(self,titulo,autor,anio):
        self.titulo=titulo
        self.autor=autor
        self.anio=anio
        print(f"libro registrado {self.titulo} de {self.autor} {self.anio}")
    def mostrar(self):
        print(f"este libro fue escrito pot {self.autor} en {self.anio}")
    def __del__(self):
        print(f"Libro eliminado {self.titulo}")
n = int(input("¿Cuántos libros deseas registrar? "))
biblioteca=[]
for i in range(n):
    print(f"\n--- Libro {i+1} ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = int(input("Año: "))

    libro = Libro(titulo, autor, anio)
    libro.mostrar()
    biblioteca.append(libro)

biblioteca.clear()
del libro
gc.collect()
print("Fin del programa")

class Departamento:
    def __init__(self,nombre):
        self.nombre = nombre
class Universidad:
    def __init__(self,nombre):
        self.nombre = nombre
        self.departamentos = []
    def agregardep(self,departamento):
        self.departamentos.append(departamento)
dep1=Departamento("INGENIERIA ESTADISTICA")
dep2=Departamento("INFORMATICA")
uni=Universidad("UNAP")
uni.agregardep(dep1)
uni.agregardep(dep2)                  


for dep in uni.departamentos:
    print(dep.nombre)

class Estudiante:
    def __init__(self,nombre,DNI,codigo):
        self.nombre = nombre
        self.DNI = DNI
        self.codigo = codigo
        self.cursos = []
    def inscribirme(self,curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.agregar_estudiante(self) 
    def info(self):
        print(f"\nEstudiante: {self.nombre} DNI: {self.DNI} codigo: {self.codigo}")
        print("cursos inscritos: ")
        for curs in self.cursos:
            print(f"{curs.nombre_curso}")

class Profesor:
    def __init__(self,nombre,DNI,especialidad):
        self.nombre = nombre
        self.DNI = DNI
        self.especialidad = especialidad
    def mostrar_r(self):
        print(f"\nProfesor: {self.nombre} DNI: {self.DNI} especialidad: {self.especialidad}")

class Curso:
    def __init__(self,nombre_curso,profesor):
        self.nombre_curso = nombre_curso
        self.profesor = profesor
        self.estudiantes = []
    def agregar_estudiante(self,estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)
    def mostrar_detalles(self):
        print(f"\nCurso: {self.nombre_curso}")
        self.profesor.mostrar_r()
        print("estudiantes inscritos:")
        for est in self.estudiantes:
            print(f"{est.nombre} {est.codigo}")

class Universidad:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cursos = []
    def agregar_cursos(self,curso):
        self.cursos.append(curso)
    def mostrar_cursos(self):
        print(f"Universidad: {self.nombre}")
        for curso in self.cursos:
            curso.mostrar_detalles()

prof1 = Profesor("Rossel Bernedo Luis Alberth", "12345678", "Matemáticas")
prof2 = Profesor("Roque Claros Roberto Elvis", "23456789", "Estadística")
prof3 = Profesor("Coyla Idme Leonel", "34567890", "Informática")
prof4 = Profesor("Vargas Valverde Confesor Milan", "45678901", "Programación")

curso1 = Curso("Matemáticas Avanzadas", prof1)
curso2 = Curso("Estadística Aplicada", prof2)
curso3 = Curso("Programación Básica", prof4)
curso4 = Curso("Sistemas Informáticos", prof3)

est1 = Estudiante("Milena Kely", "13123456", "142586")
est2 = Estudiante("Henry Quispe", "56781234", "205285")

univ = Universidad("Universidad Nacional Del Altiplano Puno")
univ.agregar_cursos(curso1)
univ.agregar_cursos(curso2)
univ.agregar_cursos(curso3)
univ.agregar_cursos(curso4)

est1.inscribirme(curso1)
est1.inscribirme(curso3)
est2.inscribirme(curso2)
est2.inscribirme(curso4)

univ.mostrar_cursos()

est1.info()
est2.info()



import tkinter as tk
import gc

class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.mostrar_texto(f"\nCurso registrado: {self.nombre} - {self.codigo} con el docente {self.profesor}")

    def mostrar_informacion(self):
        self.mostrar_texto(f"{self.nombre} con el código {self.codigo} a cargo del docente {self.profesor}")

    def __del__(self):
        self.mostrar_texto(f"Curso eliminado: {self.nombre}")

    @staticmethod
    def mostrar_texto(texto):
        salida.insert(tk.END, texto + "\n")
        salida.see(tk.END)


# Lista de cursos
wa = []

# Funciones
def registrar_curso():
    nombre = entry_nombre.get().strip()
    codigo = entry_codigo.get().strip()
    profesor = entry_profesor.get().strip()

    if not nombre or not codigo or not profesor:
        salida.insert(tk.END, "⚠️ Debes llenar todos los campos\n")
        return

    curso = Curso(nombre, codigo, profesor)
    curso.mostrar_informacion()
    wa.append(curso)

    entry_nombre.delete(0, tk.END)
    entry_codigo.delete(0, tk.END)
    entry_profesor.delete(0, tk.END)

def eliminar_cursos():
    salida.insert(tk.END, "\n--- Eliminando cursos ---\n")
    wa.clear()
    gc.collect()
    salida.insert(tk.END, "Todos los cursos fueron eliminados.\n")

def salir():
    ventana.destroy()


# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Gestión de Cursos con Input")
ventana.geometry("600x450")

frame_inputs = tk.Frame(ventana)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Nombre del curso:").grid(row=0, column=0, sticky="e")
entry_nombre = tk.Entry(frame_inputs, width=40)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Código del curso:").grid(row=1, column=0, sticky="e")
entry_codigo = tk.Entry(frame_inputs, width=40)
entry_codigo.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Profesor:").grid(row=2, column=0, sticky="e")
entry_profesor = tk.Entry(frame_inputs, width=40)
entry_profesor.grid(row=2, column=1, padx=5, pady=5)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_registrar = tk.Button(frame_botones, text="Registrar curso", command=registrar_curso, width=20)
btn_registrar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar cursos", command=eliminar_cursos, width=20)
btn_eliminar.grid(row=0, column=1, padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir, width=20)
btn_salir.grid(row=0, column=2, padx=5)

# Cuadro de salida
salida = tk.Text(ventana, height=15, width=70)
salida.pack(pady=10)

ventana.mainloop()

import tkinter as tk
from tkinter import messagebox
import gc

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print(f" Libro registrado: {self.titulo} de {self.autor} ({self.anio})")

    def mostrar(self):
        return f"{self.titulo} fue escrito por {self.autor} en {self.anio}"

    def __del__(self):
        print(f" Libro eliminado: {self.titulo}")


# Lista que almacenará los libros
biblioteca = []

# Función para agregar libros
def agregar_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    anio = entry_anio.get()

    if not titulo or not autor or not anio:
        messagebox.showwarning("Error", "Por favor, llena todos los campos.")
        return

    try:
        anio = int(anio)
    except ValueError:
        messagebox.showerror("Error", "El año debe ser un número entero.")
        return

    libro = Libro(titulo, autor, anio)
    biblioteca.append(libro)

    listbox.insert(tk.END, libro.mostrar())
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_anio.delete(0, tk.END)

# Función para eliminar libros
def eliminar_libros():
    biblioteca.clear()
    listbox.delete(0, tk.END)
    gc.collect()
    messagebox.showinfo("Biblioteca", "Todos los libros han sido eliminados.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Biblioteca - Registro de Libros")
ventana.geometry("450x400")

# Labels y Entrys
tk.Label(ventana, text="Título:").pack()
entry_titulo = tk.Entry(ventana, width=40)
entry_titulo.pack()

tk.Label(ventana, text="Autor:").pack()
entry_autor = tk.Entry(ventana, width=40)
entry_autor.pack()

tk.Label(ventana, text="Año:").pack()
entry_anio = tk.Entry(ventana, width=40)
entry_anio.pack()

# Botones
btn_agregar = tk.Button(ventana, text="Agregar Libro", command=agregar_libro)
btn_agregar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Todos", command=eliminar_libros)
btn_eliminar.pack(pady=5)

# Lista de libros
listbox = tk.Listbox(ventana, width=50, height=10)
listbox.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()

print(" Fin del programa")

class gestor_tareas:
    def __init__(self):
        self.tareas = []
    def agregar_tarea(self,tarea):
        self.tareas.append(tarea)
        print("Tarea agregada")
    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes")
        else:
            print("Traeas pendientes")
            for i, tarea in enumerate(self.tareas,1):
                print(f"{i} {tarea}")
mi_gestor = gestor_tareas()

while True:
    print ("\n-----MENU----")
    print("1. Agregar tareas")
    print("2. Mostrar tareas")
    print("3. salir")
    opcion= input("seleccione una opcion: ")

    if opcion == "1":
        tarea = input("escribe la tarea: ")
        mi_gestor.agregar_tarea(tarea)
    elif opcion == "2":
        mi_gestor.mostrar_tareas()
    elif opcion == "3":
        print("Saliendo del gestor de tareas")
        break
    else:
        print("Opcion no valida, intente denuevo")
    
    
        

class Tabla:
    def __init__(self, numero):
        self.numero = numero

    def multiplicar(self):
        for i in range(1, 11):  
            operacion = self.numero*i
            print(f"{self.numero} x {i} = {operacion}")

def main():
    numero= int(input("ingrese un numero para generar su tabla:"))
    mitabla = Tabla(numero)  
    resultadof = mitabla.multiplicar()

if __name__ == "__main__":
    main()

#suma naturales
class SN:
    def __init__(self,limite):
        self.limite = limite
        self.suma = 0
    def Calcular_suma(self):
        for i in range(1,self.limite+1):
            self.suma=self.suma+i
    
        return self.suma
def main():
    misuma=SN(10)
    resultado=misuma.Calcular_suma()
    print(f"la suma de los primeros {misuma.limite} numeros naturales es : {resultado}")
    

if __name__ == "__main__":
    main()

class Suma:
    def __init__(self,):
        self.total = 0
    def sumar_num(self):
        print("calcula la suma de numeros ingresados")
        print("escribe numeros para sumar. Escribe ¨fin¨ para terminar")
        entrada=" "
        while entrada.lower()!= "fin":
            entrada = input("ingrese un numero; ")
            if entrada.isdigit():
                self.total+=int(entrada)
            elif entrada.lower() != "fin":
                print("entrada invalida. ingrese un numerio o ¨fin¨")
        print(f"la suma total es: {self.total}")

def main():
    calculadora=Suma()
    calculadora.sumar_num()
if __name__=="__main__":
    main()


class Calculadora:
    def sumar(self,a,b):
        self.a=a
        self.b=b
        return self.a+self.b

wa = Calculadora()

suma = wa.sumar(9,4)
print(f"la suma de {wa.a} y {wa.b} es: {suma}")

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"
    def __eq__(self,otra):
        return self.edad == otra.edad
    def __gt__(self,otra):
        return self.edad > otra.edad
    def __add__(self,otra):
        return self.edad + otra.edad
persona1= Persona("Carlos",30)
persona2= Persona("Ana",25)
persona3= Persona("Lucia",30)

print(persona1)
print(persona2)
print(persona3)

print(persona1==persona2)
print(persona1==persona3)

print(persona1>persona2)
print(persona2>persona3)

print(persona1+persona2)



import math 
class circulo:
    def __init__(self,radio):
        self.radio=radio
    def area(self):
        ar=math.pi*self.radio**2
        return ar
    def perimetro(self):
        per=2*math.pi*self.radio
        return per
    def mostrar(self):
        print(f"Radio del circulo es:{self.radio}")
        print(f"el area es: {self.area():.2f}")
        print(f"el perimetro es: {self.perimetro():.2f}")
calculo=circulo(10)
calculo.mostrar()
        
        

class Operaciones:
    def sumar(self,a,b,c=None):
        if c is not None:
            return a+b+c
        else:
            return a+b
suma=Operaciones()
wa=suma.sumar(1,2,0)
dx=suma.sumar(1,2)
print(wa,dx)

class Persona:
    def __init__(self, dia, mes):
        self.dia = dia
        self.mes = mes

    def obtener_signo(self):
        if (self.mes == 3 and self.dia >= 21) or (self.mes == 4 and self.dia <= 19):
            return "Aries"
        elif (self.mes == 4 and self.dia >= 20) or (self.mes == 5 and self.dia <= 20):
            return "Tauro"
        elif (self.mes == 5 and self.dia >= 21) or (self.mes == 6 and self.dia <= 20):
            return "Géminis"
        elif (self.mes == 6 and self.dia >= 21) or (self.mes == 7 and self.dia <= 22):
            return "Cáncer"
        elif (self.mes == 7 and self.dia >= 23) or (self.mes == 8 and self.dia <= 22):
            return "Leo"
        elif (self.mes == 8 and self.dia >= 23) or (self.mes == 9 and self.dia <= 22):
            return "Virgo"
        elif (self.mes == 9 and self.dia >= 23) or (self.mes == 10 and self.dia <= 22):
            return "Libra"
        elif (self.mes == 10 and self.dia >= 23) or (self.mes == 11 and self.dia <= 21):
            return "Escorpio"
        elif (self.mes == 11 and self.dia >= 22) or (self.mes == 12 and self.dia <= 21):
            return "Sagitario"
        elif (self.mes == 12 and self.dia >= 22) or (self.mes == 1 and self.dia <= 19):
            return "Capricornio"
        elif (self.mes == 1 and self.dia >= 20) or (self.mes == 2 and self.dia <= 18):
            return "Acuario"
        elif (self.mes == 2 and self.dia >= 19) or (self.mes == 3 and self.dia <= 20):
            return "Piscis"
        else:
            return "Fecha inválida"


print("=== Calculadora de Signo Zodiacal ===")
dia = int(input("Ingresa tu día de nacimiento (1-31): "))
mes = int(input("Ingresa tu mes de nacimiento (1-12): "))

persona = Persona(dia, mes)

print("Tu signo zodiacal es:", persona.obtener_signo())

class Persona:
    def __init__(self,nombre):
        self.nombre=nombre

    def saludar(self):
        print(f"hola soy {self.nombre}")
    

persona1=Persona("Juan")
persona1.saludar()
persona2=Persona("maria")
persona2.saludar()


#clase empleado
#atributo nombre cargo salario
#accio  aplicar el aumento de sueldo (Aplicar aumento())
#gerente 10%
#supervisor 7%
#operario 5%
#otros nada
class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def AplicarAumento(self):
        if self.cargo == "Gerente":
            porcentaje = 0.10
        elif self.cargo == "Supervisor":
            porcentaje = 0.07
        elif self.cargo == "Operario":
            porcentaje = 0.05
        else:
            porcentaje = 0.0

        nuevoSalario = self.salario * (1 + porcentaje)
        return nuevoSalario
nombre = input("ingrese el nombre")
cargo = input("ingrese el cargo")
salario = float(input("ingrese el salario")

Empleado1 = Empleado("Carlos", "Gerente", 2000)
Empleado2 = Empleado("Maria", "Operario", 1200)
Empleado3 = Empleado("Ana", "Gerente", 800)
Empleado4 = Empleado("Rosa", "Supervisor", 100)

for emp in (Empleado1, Empleado2, Empleado3, Empleado4):
    salarioN = emp.AplicarAumento()
    print(f"El nuevo salario de {emp.nombre} es {salarioN:.2f}")

class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base*self.altura
    
    def calcular_perimetro(self):
        return self.base*2 + self.altura*2
    
operacion = Rectangulo(5,6)

print ("el area es:", operacion.calcular_area())
print ("el perimetro es:", operacion.calcular_perimetro())

class Profesor:
    def __init__(self,nombre):
        self.nombre = nombre



class Curso:
    def __init__(self,nombre,profesor):
        self.nombre = nombre
        self.profesor = profesor
prof=Profesor("Dr_Morillos")
curso=Curso("Muestreo",prof)
print(curso.profesor.nombre)

class Rectangulo:
    def __init__ (self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):
        return self.base*self.altura
wa=Rectangulo(10,5)
resultado=wa.area()
print("El area del rectangulo es:",resultado)

class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base*self.altura
    
    def calcular_perimetro(self):
        return self.base*2 + self.altura*2
    
operacion = Rectangulo(5,6)

print ("el area es:", operacion.calcular_area())
print ("el perimetro es:", operacion.calcular_perimetro())


class Rectangulo:
    def __init__(self,base,altura):
        self.__base=base
        self.__altura=altura
    
    
    def get_base(self):
        return slef._base
    def set_base(self,nuevo_base):
        if nuevo_base > 0:
            self.__base=nuevo_base
        else:
            print("base no  valida")
    def get_altura(self):
        return slef._altura
    def set_altura(self,nuevo_altura):
        if nuevo_altura > 0:
            self.__altura=nuevo_altura
        else:
            print("altura no  valida")
    
    def area(self):
        return self.__base*self.__altura
    def perimetro(self):
        return self.__base*2+self.__altura*2
    
    
rectangulo = Rectangulo(10,5)

print("area del circulo es:", round (rectangulo.area(),2))
print("perimetro del circulo es:",round (rectangulo.perimetro(),2))
rectangulo.set_base(19)
rectangulo.set_altura(5)
print("area del circulo es:", round (rectangulo.area(),2))
print("perimetro del circulo es:",round (rectangulo.perimetro(),2))


class Pitagoras:
    def __init__(self,catetoA,catetoB):
        self.catetoA = catetoA
        self.catetoB = catetoB

    def calcular_hipotenusa(self):
        return (self.catetoA**2 + self.catetoB**2)**(1/2)
catetoA= float(input("ingrese cateto A:"))
catetoB=float(input ("ingrese cateto B:"))

operacion = Pitagoras(catetoA,catetoB)

print ("La hipotenusa es ", operacion.calcular_hipotenusa())

import gc

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        print(f"\nProducto registrado: {self.nombre} - ${self.precio} en stock ({self.cantidad})")

    def mostrar_informacion(self):
        print(f"{self.nombre} - precio ${self.precio:.2f} en stock {self.cantidad}")

    def __del__(self):
        print(f"Producto eliminado: {self.nombre}")

producto_datos = [
    ("Manzana", 0.5, 100),
    ("Pan", 0.3, 50),
    ("Leche", 3.50, 30)
]

inventario = []


for datos in producto_datos:
    producto = Producto(*datos)
    producto.mostrar_informacion()
    inventario.append(producto)



print("\nVaciando inventario...")
inventario.clear()   
del producto
gc.collect()         

print("Fin del programa")

class Producto:
    def __init__(self,nombre,precio,stock):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
    def __str__(self):
        return f"{self.nombre} {self.precio} {self.stock}"
    def __eq__(self,otro):
        return self.nombre==otro.nombre
    def __add__(self,otro):
        return self.precio+self.precio
prod=Producto("Arroz",3.50,20)
prod1=Producto("Arroz",3.50,15)
prod2=Producto("Azucar",4.00,10)

print(prod)
print(prod==prod1)
print(prod+prod1)


import math
class Triangulo:
    def __init__(self,catA,catB):
        self.catA=catA
        self.catB=catB
    def pitagoras(self):
        return math.sqrt(self.catA**2+self.catB**2)
wa=Triangulo(3,4)
resultado=wa.pitagoras()
print("La hipotenusa es:",resultado)

#clase persona
#atributo nombre
#accion si es o no mayor de edad
#onjeto persona Maria 25
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
nombre= input("ingrese el nombre de la persona:")
edad= float(input("ingrese la edad de la persona:"))
persona= Persona(nombre,edad)
if persona.es_mayor_de_edad():
    print(f"{persona.nombre} es mayor de edad")
else:
    print(f"{persona.nombre} es menor de edad")

