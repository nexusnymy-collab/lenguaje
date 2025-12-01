# ----------------------------------------------------
# TRABAJO 2 - LENGUAJE DE PROGRAMACIÓN
# Alumno: nexu yohan mamani yucra
# ----------------------------------------------------

# ===============================
# 1. Clases y Objetos
# ===============================

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
        else:
            print("No se puede retirar ese monto.")

    def mostrar(self):
        print("Titular:", self.titular, "| Saldo:", self.saldo)


# Prueba
c1 = CuentaBancaria("Luis", 500)
c1.depositar(200)
c1.retirar(100)
c1.mostrar()


# ===============================
# 2. Encapsulamiento
# ===============================

class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self.precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor >= 0:
            self._precio = valor
        else:
            print("Precio inválido.")
            self._precio = 0

    def aplicar_descuento(self, porcentaje):
        if 0 <= porcentaje <= 100:
            self._precio -= self._precio * (porcentaje / 100)


p1 = Producto("Mouse", 80)
p1.aplicar_descuento(10)
print("Precio mouse:", p1.precio)


# ===============================
# 3. Herencia Simple
# ===============================

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_pago(self):
        return self.salario


class EmpleadoTiempoCompleto(Empleado):
    pass


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, tarifa, horas):
        super().__init__(nombre, tarifa)
        self.horas = horas

    def calcular_pago(self):
        return self.salario * self.horas


e1 = EmpleadoTiempoCompleto("Ana", 1800)
e2 = EmpleadoPorHoras("Luis", 20, 80)

print(e1.nombre, e1.calcular_pago())
print(e2.nombre, e2.calcular_pago())


# ===============================
# 4. Herencia Múltiple (VERSIÓN SOLICITADA)
# ===============================

class Vehiculo:
    def acelerar(self):
        print("El avión está acelerando.")


class Volador:
    def volar(self):
        print("El avión está volando.")


class Avion(Vehiculo, Volador):
    def activar(self):
        print("El avión está acelerando y volando al mismo tiempo.")


# Prueba
avion = Avion()
avion.activar()


# ===============================
# 5. Polimorfismo
# ===============================

import math

class Figura:
    def area(self):
        pass


class Rectangulo(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)


figs = [
    Rectangulo(4, 5),
    Triangulo(4, 6),
    Circulo(3)
]

for f in figs:
    print("Área:", f.area())


# ===============================
# 6. Sobrecarga de Operadores
# ===============================

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector2D(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        return Vector2D(self.x - otro.x, self.y - otro.y)

    def __mul__(self, escalar):
        return Vector2D(self.x * escalar, self.y * escalar)

    def __repr__(self):
        return f"({self.x}, {self.y})"


v1 = Vector2D(2, 3)
v2 = Vector2D(5, 1)

print("Suma:", v1 + v2)
print("Resta:", v1 - v2)
print("Escalar:", v1 * 2)


# ===============================
# 7. Composición
# ===============================

class Motor:
    def encender(self):
        print("Motor encendido.")


class Auto:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        print("Arrancando...")
        self.motor.encender()


auto = Auto()
auto.arrancar()


# ===============================
# 8. Métodos Estáticos y de Clase
# ===============================

class ConversorTemperatura:
    def __init__(self, f):
        self.fahrenheit = f

    @staticmethod
    def c_a_f(c):
        return (c * 9/5) + 32

    @classmethod
    def desde_celsius(cls, c):
        return cls(cls.c_a_f(c))


t1 = ConversorTemperatura.desde_celsius(30)
print("Fahrenheit:", t1.fahrenheit)


# ===============================
# 9. Excepciones Personalizadas
# ===============================

class DivisionPorCeroError(Exception):
    pass


class CalculadoraSegura:
    def dividir(self, a, b):
        if b == 0:
            raise DivisionPorCeroError("No se puede dividir entre cero.")
        return a / b


calc = CalculadoraSegura()
try:
    print(calc.dividir(10, 0))
except DivisionPorCeroError as e:
    print("Error:", e)


# ===============================
# 10. Clases Abstractas (VERSIÓN SOLICITADA)
# ===============================

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        print("El perro hace el sonido: guau")


class Gato(Animal):
    def hacer_sonido(self):
        print("El gato hace el sonido: miau")


# Prueba
animales = [Perro(), Gato()]
for a in animales:
    a.hacer_sonido()


    
