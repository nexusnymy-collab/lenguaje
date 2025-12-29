from datetime import datetime

# Clase Producto
class Producto:
    def __init__(self, codigo, nombre, precio, cantidad=0, categoria="", proveedor="", descripcion=""):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
        self.proveedor = proveedor
        self.descripcion = descripcion

    def __str__(self):
        return (f"{self.codigo} | {self.nombre} | Precio: {self.precio} | Stock: {self.cantidad} "
                f"| Categoría: {self.categoria} | Proveedor: {self.proveedor} | Desc: {self.descripcion}")

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self, producto):
        if producto.codigo in self.productos:
            print("El producto ya existe. Actualizando información.")
        self.productos[producto.codigo] = producto
        print(f"Producto '{producto.nombre}' registrado correctamente.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("\nInventario Actual:")
        print("-"*80)
        for producto in self.productos.values():
            print(producto)
        print("-"*80)

    def entrada_stock(self, codigo, cantidad):
        if codigo in self.productos:
            self.productos[codigo].cantidad += cantidad
            print(f"Entrada registrada. Nuevo stock de '{self.productos[codigo].nombre}': {self.productos[codigo].cantidad}")
        else:
            print("Producto no encontrado.")

    def salida_stock(self, codigo, cantidad):
        if codigo in self.productos:
            if self.productos[codigo].cantidad >= cantidad:
                self.productos[codigo].cantidad -= cantidad
                print(f"Salida registrada. Nuevo stock de '{self.productos[codigo].nombre}': {self.productos[codigo].cantidad}")
            else:
                print("No hay suficiente stock para realizar la salida.")
        else:
            print("Producto no encontrado.")

    def generar_reporte(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\nReporte de Inventario - {now}")
        print("-"*80)
        total_valor = 0
        for producto in self.productos.values():
            valor = producto.precio * producto.cantidad
            total_valor += valor
            print(f"{producto.nombre} | Stock: {producto.cantidad} | Valor total: {valor} | Categoría: {producto.categoria} | Proveedor: {producto.proveedor}")
        print("-"*80)
        print(f"Valor total del inventario: {total_valor}\n")

# Clase principal
class SistemaInventario:
    def __init__(self):
        self.inventario = Inventario()

    def menu(self):
        while True:
            print("\n--- Sistema de Inventario ---")
            print("1. Registrar Producto")
            print("2. Mostrar Inventario")
            print("3. Entrada de Stock")
            print("4. Salida de Stock")
            print("5. Generar Reporte")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                codigo = input("Código del producto: ")
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad inicial: "))
                categoria = input("Categoría del producto: ")
                proveedor = input("Proveedor: ")
                descripcion = input("Descripción corta: ")
                producto = Producto(codigo, nombre, precio, cantidad, categoria, proveedor, descripcion)
                self.inventario.registrar_producto(producto)

            elif opcion == "2":
                self.inventario.mostrar_inventario()

            elif opcion == "3":
                codigo = input("Código del producto: ")
                cantidad = int(input("Cantidad a ingresar: "))
                self.inventario.entrada_stock(codigo, cantidad)

            elif opcion == "4":
                codigo = input("Código del producto: ")
                cantidad = int(input("Cantidad a retirar: "))
                self.inventario.salida_stock(codigo, cantidad)

            elif opcion == "5":
                self.inventario.generar_reporte()

            elif opcion == "6":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

# Ejecución del sistema
if __name__ == "__main__":
    sistema = SistemaInventario()
    sistema.menu()
