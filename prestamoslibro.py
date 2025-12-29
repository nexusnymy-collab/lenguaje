from datetime import datetime

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
        self.fecha_prestamo = None
        self.fecha_devolucion = None
        self.usuario = None

    def prestar(self, usuario):
        if self.disponible:
            self.disponible = False
            self.usuario = usuario
            self.fecha_prestamo = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"\n📕 El libro '{self.titulo}' ha sido prestado a {self.usuario} el {self.fecha_prestamo}.")
        else:
            print(f"\n❌ El libro '{self.titulo}' ya fue prestado a {self.usuario} el {self.fecha_prestamo}.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            self.fecha_devolucion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"✅ El libro '{self.titulo}' ha sido devuelto por {self.usuario} el {self.fecha_devolucion}.")
            self.usuario = None
        else:
            print(f"⚠️ El libro '{self.titulo}' ya estaba disponible.")

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else f"Prestado a {self.usuario}"
        print(f"\n📘 Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Estado: {estado}")
        if self.fecha_prestamo:
            print(f"Fecha de préstamo: {self.fecha_prestamo}")
        if self.fecha_devolucion:
            print(f"Fecha de devolución: {self.fecha_devolucion}")
        print("-" * 40)


# --- Programa principal ---

# Libros registrados automáticamente
libros = [
    Libro("Cien años de soledad", "Gabriel García Márquez"),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes")
]

print("\n--- ESTADO INICIAL DE LOS LIBROS ---")
for libro in libros:
    libro.mostrar_info()

# Registrar préstamos (solo ingresar usuario)
print("\n--- REGISTRO DE PRÉSTAMOS ---")
for libro in libros:
    usuario = input(f"Ingrese el nombre del usuario que pide prestado '{libro.titulo}': ")
    libro.prestar(usuario)

# Mostrar después del préstamo
print("\n--- ESTADO DESPUÉS DEL PRÉSTAMO ---")
for libro in libros:
    libro.mostrar_info()

# Registrar devoluciones
print("\n--- REGISTRO DE DEVOLUCIONES ---")
for libro in libros:
    devolver = input(f"¿Desea registrar la devolución del libro '{libro.titulo}'? (s/n): ").lower()
    if devolver == "s":
        libro.devolver()

# Estado final
print("\n--- ESTADO FINAL DE LOS LIBROS ---")
for libro in libros:
    libro.mostrar_info()
