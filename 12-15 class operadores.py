# Principio S
class CalculadoraOperacion:
    def calcular(self):
        raise NotImplementedError("Debe implementar el metodo calcular")


# Principios O y L
class Suma(CalculadoraOperacion):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a + self.b


class Resta(CalculadoraOperacion):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a - self.b


class Multiplicacion(CalculadoraOperacion):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a * self.b


class Division(CalculadoraOperacion):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        if self.b == 0:
            return "Error: división entre cero"
        return self.a / self.b


# Principio D
class Aplicacion:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def ejecutar(self):
        resultado = self.calculadora.calcular()
        print(f"El resultado es: {resultado}")


# ================== INPUT DEL USUARIO ==================
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

print("Seleccione la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Opción: ")

if opcion == "1":
    operacion = Suma(a, b)
elif opcion == "2":
    operacion = Resta(a, b)
elif opcion == "3":
    operacion = Multiplicacion(a, b)
elif opcion == "4":
    operacion = Division(a, b)
else:
    print("Opción no válida")
    exit()

app = Aplicacion(operacion)
app.ejecutar()
