import math
import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Calculadora:
    def __init__(self):
        self.datos = []
        self.cantidad = 0
        self.suma = 0

    def media_muestral(self):
        self.suma = sum(self.datos)
        self.cantidad = len(self.datos)
        media = self.suma / self.cantidad
        return media

    def varianza_muestral(self, media):
        varianza = sum((dato - media) ** 2 for dato in self.datos)
        varianza = varianza / (self.cantidad - 1)
        return varianza

    def desviacion_estandar(self, varianza):
        return math.sqrt(varianza)


def calcular():
    try:
        raw = entry_datos.get()
        # Limpiar y separar los valores por coma, ignorando entradas vacías
        items = [s.strip() for s in raw.split(",")]
        items = [s for s in items if s != ""]
        if not items:
            raise ValueError("No ingresaste datos válidos.")

        datos = [float(x) for x in items]

        aplicar = Calculadora()
        aplicar.datos = datos

        media = aplicar.media_muestral()

        # Si hay menos de 2 datos no se puede calcular la varianza muestral (n-1 = 0)
        if aplicar.cantidad < 2:
            messagebox.showinfo("Atención", "Se necesita al menos 2 datos para calcular la varianza muestral.")
            varianza = float("nan")
            desviacion = float("nan")
        else:
            varianza = aplicar.varianza_muestral(media)
            desviacion = aplicar.desviacion_estandar(varianza)

        # Mostrar resultados
        label_resultados.config(
            text=(f"Media muestral: {media:.4f}\n"
                  f"Varianza muestral: {varianza:.4f}\n"
                  f"Desviación estándar: {desviacion:.4f}")
        )

        # Eliminar la gráfica anterior si existe
        if hasattr(ventana, "canvas_widget") and ventana.canvas_widget is not None:
            ventana.canvas_widget.destroy()
            ventana.canvas_widget = None
            ventana.canvas = None

        # Graficar los datos
        fig = Figure(figsize=(6, 3.5), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(datos, marker="o", linestyle="-", label="Datos")
        ax.axhline(y=media, linestyle="--", label="Media")
        ax.set_title("Gráfico de los datos")
        ax.set_xlabel("Índice")
        ax.set_ylabel("Valor")
        ax.legend()

        # Integrar la gráfica en Tkinter
        canvas = FigureCanvasTkAgg(fig, master=ventana)
        canvas.draw()
        widget = canvas.get_tk_widget()
        widget.pack(pady=10)
        ventana.canvas_widget = widget
        ventana.canvas = canvas

    except ValueError as ve:
        messagebox.showerror("Error de entrada", str(ve))
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))


# --- Interfaz ---
ventana = tk.Tk()
ventana.title("Calculadora Estadística")
ventana.geometry("700x500")
ventana.canvas_widget = None
ventana.canvas = None

tk.Label(ventana, text="Introduce los datos separados por comas (ej: 10, 20, 30):").pack(pady=6)
entry_datos = tk.Entry(ventana, width=70)
entry_datos.pack(padx=10)

btn = tk.Button(ventana, text="Calcular", command=calcular)
btn.pack(pady=10)

label_resultados = tk.Label(ventana, text="", font=("Arial", 12), justify="left")
label_resultados.pack()

ventana.mainloop()
