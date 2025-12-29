import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import datetime
import random
import sqlite3

# ======== CLASES DE PAGO =========
class MetodoPago:
    def __init__(self, monto):
        self.monto = monto
    def pagar(self):
        return f"Procesando pago de S/. {self.monto:.2f}"

class TarjetaCredito(MetodoPago):
    def __init__(self, monto, numero, nombre, cvv, vencimiento):
        super().__init__(monto)
        self.numero, self.nombre, self.cvv, self.venc = numero, nombre, cvv, vencimiento
    def pagar(self):
        return (f"💳 Tarjeta de Crédito\n"
                f"Titular: {self.nombre}\n"
                f"Número: ****{self.numero[-4:]}\n"
                f"Vence: {self.venc}")

class PayPal(MetodoPago):
    def __init__(self, monto, correo):
        super().__init__(monto)
        self.correo = correo
    def pagar(self):
        return f"🌐 PayPal\nCuenta: {self.correo}"

class Efectivo(MetodoPago):
    def __init__(self, monto, nombre):
        super().__init__(monto)
        self.nombre = nombre
    def pagar(self):
        return f"💵 Efectivo\nCliente: {self.nombre}"

class Yape(MetodoPago):
    def __init__(self, monto, numero, nombre):
        super().__init__(monto)
        self.numero, self.nombre = numero, nombre
    def pagar(self):
        return f"📱 Yape\nTitular: {self.nombre}\nNúmero: {self.numero}"

# ======== BASE DE DATOS =========
def inicializar_db():
    conn = sqlite3.connect("pagos.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pagos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            metodo TEXT,
            monto REAL,
            codigo TEXT
        )
    """)
    conn.commit()
    conn.close()

def guardar_pago_db(fecha, metodo, monto, codigo):
    conn = sqlite3.connect("pagos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pagos (fecha, metodo, monto, codigo) VALUES (?, ?, ?, ?)",
                   (fecha, metodo, monto, codigo))
    conn.commit()
    conn.close()

def cargar_historial_db():
    conn = sqlite3.connect("pagos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT fecha, metodo, monto, codigo FROM pagos ORDER BY id DESC")
    pagos = cursor.fetchall()
    conn.close()
    return pagos

# ======== FUNCIONES PRINCIPALES =========
baucher_actual = ""  # guardará el texto del último baucher

def mostrar_baucher(metodo, detalle, monto):
    """Muestra y conserva el baucher en pantalla"""
    global baucher_actual
    fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    codigo = f"TRX-{random.randint(100000,999999)}"
    baucher_actual = f"""
----------------------------------------------
              💰 BAUCHER DE PAGO 💰
----------------------------------------------
Fecha/Hora : {fecha}
Transacción: {codigo}
Método     : {metodo}
Monto      : S/. {monto:.2f}
----------------------------------------------
{detalle}
----------------------------------------------
¡Gracias por su preferencia! 🙌
----------------------------------------------
"""
    # Mostrar el baucher (no se borra)
    text_ticket.config(state="normal")
    text_ticket.insert(tk.END, baucher_actual + "\n")
    text_ticket.config(state="disabled")

    guardar_pago_db(fecha, metodo, monto, codigo)
    tabla_historial.insert("", 0, values=(fecha, metodo, f"S/. {monto:.2f}", codigo))

def guardar_baucher():
    """Permite guardar el baucher actual en un archivo .txt"""
    global baucher_actual
    if not baucher_actual.strip():
        messagebox.showwarning("Atención", "No hay ningún baucher para guardar.")
        return
    ruta = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivo de texto", "*.txt")],
        title="Guardar baucher como"
    )
    if ruta:
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(baucher_actual)
        messagebox.showinfo("Guardado ✅", f"Baucher guardado en:\n{ruta}")

def actualizar_campos(*args):
    for w in [lbl_2, entry_2, lbl_3, entry_3, lbl_4, entry_4, lbl_5, entry_5]:
        w.grid_remove()
    m = metodo_var.get()
    if m == "Tarjeta de Crédito":
        lbl_2.config(text="N° tarjeta:"); lbl_2.grid(row=3, column=0); entry_2.grid(row=3, column=1)
        lbl_3.config(text="Titular:"); lbl_3.grid(row=4, column=0); entry_3.grid(row=4, column=1)
        lbl_4.config(text="CVV:"); lbl_4.grid(row=5, column=0); entry_4.grid(row=5, column=1)
        lbl_5.config(text="Vencimiento:"); lbl_5.grid(row=6, column=0); entry_5.grid(row=6, column=1)
    elif m == "PayPal":
        lbl_2.config(text="Correo PayPal:"); lbl_2.grid(row=3, column=0); entry_2.grid(row=3, column=1)
    elif m == "Efectivo":
        lbl_2.config(text="Nombre del cliente:"); lbl_2.grid(row=3, column=0); entry_2.grid(row=3, column=1)
    elif m == "Yape":
        lbl_2.config(text="Número:"); lbl_2.grid(row=3, column=0); entry_2.grid(row=3, column=1)
        lbl_3.config(text="Titular:"); lbl_3.grid(row=4, column=0); entry_3.grid(row=4, column=1)

def limpiar_campos():
    entry_1.delete(0, tk.END)
    for e in [entry_2, entry_3, entry_4, entry_5]:
        e.delete(0, tk.END)

def realizar_pago():
    """Procesa el pago, muestra el baucher y guarda en DB"""
    metodo = metodo_var.get()
    try:
        monto = float(entry_1.get())
        if monto <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Monto inválido."); return

    d = [entry_2.get().strip(), entry_3.get().strip(), entry_4.get().strip(), entry_5.get().strip()]
    if metodo == "Tarjeta de Crédito":
        if not all(d[:4]): return messagebox.showerror("Error","Complete todos los datos de tarjeta.")
        pago = TarjetaCredito(monto, d[0], d[1], d[2], d[3])
    elif metodo == "PayPal":
        if not d[0]: return messagebox.showerror("Error","Ingrese el correo de PayPal.")
        pago = PayPal(monto, d[0])
    elif metodo == "Efectivo":
        if not d[0]: return messagebox.showerror("Error","Ingrese el nombre del cliente.")
        pago = Efectivo(monto, d[0])
    elif metodo == "Yape":
        if not all(d[:2]): return messagebox.showerror("Error","Ingrese número y titular.")
        pago = Yape(monto, d[0], d[1])
    else:
        return messagebox.showerror("Error","Seleccione un método de pago.")

    detalle = pago.pagar()
    mostrar_baucher(metodo, detalle, monto)
    messagebox.showinfo("Pago Exitoso ✅", "El pago se procesó correctamente.")
    limpiar_campos()

# ======== INTERFAZ TKINTER =========
root = tk.Tk()
root.title("💳 Sistema de Pagos con Base de Datos y Baucher Guardable")
root.geometry("750x900")
root.configure(bg="#f0f4ff")

frm = ttk.Frame(root, padding=15)
frm.pack(fill="x", pady=10)

metodo_var = tk.StringVar()
metodo_var.trace("w", actualizar_campos)

ttk.Label(frm, text="Método de pago:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5)
combo = ttk.Combobox(frm, textvariable=metodo_var,
                     values=["Tarjeta de Crédito", "PayPal", "Efectivo", "Yape"], state="readonly", width=25)
combo.grid(row=0, column=1, padx=5, pady=5)
combo.set("Tarjeta de Crédito")

ttk.Label(frm, text="Monto (S/.):").grid(row=2, column=0, padx=5, pady=5)
entry_1 = ttk.Entry(frm, width=28)
entry_1.grid(row=2, column=1, padx=5, pady=5)

lbl_2, lbl_3, lbl_4, lbl_5 = [ttk.Label(frm) for _ in range(4)]
entry_2, entry_3, entry_4, entry_5 = [ttk.Entry(frm, width=28) for _ in range(4)]

ttk.Button(frm, text="💰 Realizar Pago", command=realizar_pago).grid(row=8, column=0, columnspan=2, pady=10)
ttk.Button(frm, text="💾 Guardar Baucher", command=guardar_baucher).grid(row=9, column=0, columnspan=2, pady=5)

# Baucher
frame_ticket = ttk.LabelFrame(root, text="🧾 Baucher Generado", padding=10)
frame_ticket.pack(fill="both", expand=True, padx=20, pady=10)
text_ticket = tk.Text(frame_ticket, width=85, height=15, state="disabled", bg="white", fg="black", font=("Courier", 10))
text_ticket.pack(pady=5)

# Historial
frame_historial = ttk.LabelFrame(root, text="📜 Historial de Pagos", padding=10)
frame_historial.pack(fill="both", expand=True, padx=20, pady=10)
columnas = ("fecha", "metodo", "monto", "codigo")
tabla_historial = ttk.Treeview(frame_historial, columns=columnas, show="headings", height=8)
tabla_historial.pack(fill="both", expand=True)

for col, ancho in zip(columnas, (180, 120, 100, 120)):
    tabla_historial.heading(col, text=col.capitalize())
    tabla_historial.column(col, width=ancho, anchor="center")

# Iniciar base de datos y cargar historial
inicializar_db()
for fila in cargar_historial_db():
    tabla_historial.insert("", 0, values=(fila[0], fila[1], f"S/. {fila[2]:.2f}", fila[3]))

actualizar_campos()
root.mainloop()9
