import tkinter as tk
from tkinter import ttk, messagebox

# ==============================
# CLASES BASE
# ==============================
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

class Trabajador:
    def __init__(self, profesion, salario):
        self.profesion = profesion
        self.salario = salario

    def trabajar(self):
        return f"Estoy trabajando como {self.profesion} y gano ${self.salario} al mes."

class Estudiante:
    def __init__(self, carrera, universidad):
        self.carrera = carrera
        self.universidad = universidad

    def estudiar(self):
        return f"Estudio {self.carrera} en la universidad {self.universidad}."

# ==============================
# CLASE MULTIROL
# ==============================
class PersonaMultirol(Persona, Trabajador, Estudiante):
    def __init__(self, nombre, edad, profesion, salario, carrera, universidad):
        Persona.__init__(self, nombre, edad)
        Trabajador.__init__(self, profesion, salario)
        Estudiante.__init__(self, carrera, universidad)

    def mostrar_informacion(self):
        info = "===== INFORMACIÓN DE LA PERSONA =====\n"
        info += self.presentarse() + "\n"
        info += self.trabajar() + "\n"
        info += self.estudiar() + "\n"
        return info

# ==============================
# FUNCIÓNES DE INTERFAZ
# ==============================
personas = []  # lista global para almacenar personas agregadas

def agregar_persona():
    try:
        nombre = entry_nombre.get()
        edad = int(entry_edad.get())
        profesion = entry_profesion.get()
        salario = float(entry_salario.get())
        carrera = entry_carrera.get()
        universidad = entry_universidad.get()

        if not nombre or not profesion or not carrera or not universidad:
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return

        nueva_persona = PersonaMultirol(nombre, edad, profesion, salario, carrera, universidad)
        personas.append(nueva_persona)

        messagebox.showinfo("Éxito", f"Se agregó a {nombre} correctamente.")

        # limpiar campos
        for e in [entry_nombre, entry_edad, entry_profesion, entry_salario, entry_carrera, entry_universidad]:
            e.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Verifica los valores numéricos (edad y salario).")

def mostrar_todas():
    if not personas:
        messagebox.showinfo("Sin datos", "No se han agregado personas aún.")
        return

    text_resultado.config(state="normal")
    text_resultado.delete(1.0, tk.END)

    for i, persona in enumerate(personas, start=1):
        text_resultado.insert(tk.END, f"--- PERSONA {i} ---\n")
        text_resultado.insert(tk.END, persona.mostrar_informacion() + "\n")

    text_resultado.config(state="disabled")

def limpiar_lista():
    personas.clear()
    text_resultado.config(state="normal")
    text_resultado.delete(1.0, tk.END)
    text_resultado.config(state="disabled")
    messagebox.showinfo("Limpieza", "Se han borrado todas las personas registradas.")

# ==============================
# CONFIGURAR VENTANA PRINCIPAL
# ==============================
ventana = tk.Tk()
ventana.title("Gestor de Personas Multirol")
ventana.geometry("650x700")
ventana.resizable(False, False)

# Título
ttk.Label(ventana, text="REGISTRO DE PERSONAS", font=("Arial", 14, "bold")).pack(pady=10)

# Frame principal de entrada
frame = ttk.Frame(ventana, padding=10)
frame.pack(fill="x", padx=10, pady=5)

labels = ["Nombre:", "Edad:", "Profesión:", "Salario ($):", "Carrera:", "Universidad:"]
entries = []

for i, text in enumerate(labels):
    ttk.Label(frame, text=text).grid(row=i, column=0, sticky="e", pady=4)
    entry = ttk.Entry(frame, width=45)
    entry.grid(row=i, column=1)
    entries.append(entry)

entry_nombre, entry_edad, entry_profesion, entry_salario, entry_carrera, entry_universidad = entries

# ==============================
# BOTONES
# ==============================
frame_botones = ttk.Frame(ventana)
frame_botones.pack(pady=10)

ttk.Button(frame_botones, text="Agregar Persona", command=agregar_persona).grid(row=0, column=0, padx=5)
ttk.Button(frame_botones, text="Mostrar Todas", command=mostrar_todas).grid(row=0, column=1, padx=5)
ttk.Button(frame_botones, text="Limpiar Lista", command=limpiar_lista).grid(row=0, column=2, padx=5)

# ==============================
# ÁREA DE RESULTADO
# ==============================
ttk.Label(ventana, text="INFORMACIÓN REGISTRADA:", font=("Arial", 11, "bold")).pack(pady=5)
text_resultado = tk.Text(ventana, height=20, width=80, wrap="word", state="disabled")
text_resultado.pack(padx=10, pady=10)

# ==============================
# INICIAR APP
# ==============================
ventana.mainloop()
