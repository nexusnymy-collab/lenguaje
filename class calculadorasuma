class CalculadoraSuma:
    def __init__(self):
        self.total = 0
    
    def sumarNumeros(self):
        print("Calcula la suma de numeros ingresado")
        print("Escribe numeros para sumar. Escribe 'fin' para terminar")
        
        while True:
            entrada = input("Ingrese un numero : ")
            
            if entrada.lower() == 'fin':
                break
            
            if entrada.isdigit():
                self.total += int(entrada)
            else:
                print("Entrada invalida: Escriba un numero o 'fin'")
        
        print(f"La suma total es: {self.total}")

def main():
    calculadora = CalculadoraSuma()
    calculadora.sumarNumeros()

if __name__ == "__main__":
    main()
