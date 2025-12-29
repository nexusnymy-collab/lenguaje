from typing import TypeVar, Generic

T = TypeVar('T', int, float)

class triangulorectangulo(Generic[T]):
    def __init__(self, cateto1,cateto2: T):
        self.cateto1=cateto1
        self.cateto2=cateto2

    def calcular_hipotenusa(self) -> int:
        n = int(self.cateto1**2+self.cateto2**2)

        if n < 0:
            raise ValueError("")

        resultado = 1
        for i in range(1, n + 1):
            resultado *= i

        return resultado


def main():
    try:
        n = int(input("Ingrese un número: "))
        cal = triangulorectagulo(n)
        print(f"El factorial de {n} es: {cal.calcular_factorial()}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
