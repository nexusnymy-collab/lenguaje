import tkinter as tk
from tkinter import ttk, messagebox
import math

# --- Funciones geométricas ---
def calcular():
    figura = figura_var.get()
    try:
        canvas.delete("all")  # Limpiar dibujo
        if figura == "Cuadrado":
            lado = float(entry_1.get())
            area = lado ** 2
            perimetro = 4 * lado

            # Dibujo (escala para que se vea bien)
            lado_px = lado * 20
            canvas.create_rectangle(50, 50, 50 + lado_px, 50 + lado_px,
                                    fill="skyblue", outline="blue", width=3)
            canvas.create_text(50 + lado_px / 2, 50 + lado_px + 20,
                               text=f"Lado = {lado}", font=("Arial", 10, "bold"))

        elif figura == "Círculo":
            radio = float(entry_1.get())
            area = math.pi * radio ** 2
            perimetro = 2 * math.pi * radio

            radio_px = radio * 20
            canvas.create_oval(150 - radio_px, 100 - radio_px,
                               150 + radio_px, 100 + radio_px,
                               fill="lightgreen", outline="green", width=3)
            canvas.create_text(150, 100 + radio_px + 20,
                               text=f"Radio = {radio}", font=("Arial", 10, "bold"))

        elif figura == "Triángulo":
            base = float(entry_1.get())
            altura = float(entry_2.get())
            area = (base * altura) / 2
            lado = math.sqrt((base / 2) ** 2 + altura ** 2)
            perimetro = base + 2 * lado

            base_px = base * 20
            altura_px = altura * 20
            canvas.create_polygon(100, 200, 100 + base_px, 200,
                                  100 + base_px / 2, 200 - altura_px,
                                  fill="pink", outline="red", width=3)
            canvas.create_text(100 + base_px / 2, 210,
                               text=f"Base = {base}", font=("Arial", 10, "bold"))
            canvas.create_text(100 + base_px / 2, 200 - altura_px - 15,
                               text=f"Altura = {altura}", font=("Arial", 10, "bold"))

        else:
            messagebox.showerror("Error", "Selecciona una figura.")
            return

        lbl_resultado.config(
            text=f"Área = {area:.2f} | Perímetro = {perimetro:.2f}"
        )

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

def actualizar_campos(*args):
    """Muestra los campos correctos según la figura"""
    figura = figura_var.get()
    if figura == "Triángulo":
        lbl_1.config(text="Base:")
        lbl_2.grid(row=3, column=0, padx=5, pady=5)
        entry_2.grid(row=3, column=1, padx=5, pady=5)
        lbl_2.config(text="Altura:")
    elif figura == "Círculo":
        lbl_1.config(text="Radio:")
        lbl_2.grid_remove()
        entry_2.grid_remove()
    else:  # Cuadrado
        lbl_1.config(text="Lado:")
        lbl_2.grid_remove()
        entry_2.grid_remove()

# --- Interfaz gráfica ---
root = tk.Tk()
root.title("Calculadora de Figuras 2D")
root.geometry("500x500")
root.resizable(False, False)

figura_var = tk.StringVar()
figura_var.trace("w", actualizar_campos)

frm = ttk.Frame(root, padding=10)
frm.pack(fill="x")

ttk.Label(frm, text="Selecciona una figura:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5)
combo = ttk.Combobox(frm, textvariable=figura_var, values=["Cuadrado", "Círculo", "Triángulo"], state="readonly")
combo.grid(row=0, column=1, padx=5, pady=5)
combo.set("Cuadrado")

lbl_1 = ttk.Label(frm, text="Lado:")
lbl_1.grid(row=2, column=0, padx=5, pady=5)
entry_1 = ttk.Entry(frm)
entry_1.grid(row=2, column=1, padx=5, pady=5)

lbl_2 = ttk.Label(frm, text="Altura:")
entry_2 = ttk.Entry(frm)

ttk.Button(frm, text="Calcular", command=calcular).grid(row=4, column=0, columnspan=2, pady=10)

lbl_resultado = ttk.Label(frm, text="", font=("Arial", 12, "bold"), foreground="darkblue")
lbl_resultado.grid(row=5, column=0, columnspan=2, pady=10)

# Canvas para dibujo
canvas = tk.Canvas(root, width=400, height=250, bg="white")
canvas.pack(pady=10)

root.mainloop()
