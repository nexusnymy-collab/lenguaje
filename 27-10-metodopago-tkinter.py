import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import random

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

# ======== FUNCIONES =========
def mostrar_baucher(metodo, detalle, monto):
    """Muestra el baucher directamente en pantalla"""
    fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    codigo = f"TRX-{random.randint(100000,999999)}"
    ticket = f"""
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
    text_ticket.config(state="normal")
    text_ticket.delete(1.0, tk.END)
    text_ticket.insert(tk.END, ticket)
    text_ticket.config(state="disabled")

def actualizar_campos(*args):
    """Actualiza los campos según el método de pago seleccionado"""
    for w in [lbl_2, entry_2, lbl_3, entry_3, lbl_4, entry_4, lbl_5, entry_5]:
        w.grid_remove()
    m = metodo_var.get()
    if m == "Tarjeta de Crédito":
        lbl_2.config(text="N° tarjeta:"); lbl_2.grid(row=3, column=0, pady=3); entry_2.grid(row=3, column=1, pady=3)
        lbl_3.config(text="Titular:"); lbl_3.grid(row=4, column=0, pady=3); entry_3.grid(row=4, column=1, pady=3)
        lbl_4.config(text="CVV:"); lbl_4.grid(row=5, column=0, pady=3); entry_4.grid(row=5, column=1, pady=3)
        lbl_5.config(text="Vencimiento:"); lbl_5.grid(row=6, column=0, pady=3); entry_5.grid(row=6, column=1, pady=3)
    elif m == "PayPal":
        lbl_2.config(text="Correo PayPal:"); lbl_2.grid(row=3, column=0, pady=3); entry_2.grid(row=3, column=1, pady=3)
    elif m == "Efectivo":
        lbl_2.config(text="Nombre del cliente:"); lbl_2.grid(row=3, column=0, pady=3); entry_2.grid(row=3, column=1, pady=3)
    elif m == "Yape":
        lbl_2.config(text="Número:"); lbl_2.grid(row=3, column=0, pady=3); entry_2.grid(row=3, column=1, pady=3)
        lbl_3.config(text="Titular:"); lbl_3.grid(row=4, column=0, pady=3); entry_3.grid(row=4, column=1, pady=3)

def realizar_pago():
    """Procesa el pago y muestra el baucher"""
    metodo = metodo_var.get()
    try:
        monto = float(entry_1.get())
        if monto <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Monto inválido."); return

    d = [entry_2.get().strip(), entry_3.get().strip(), entry_4.get().strip(), entry_5.get().strip()]
    if metodo == "Tarjeta de Crédito":
        if not all(d[:4]): return messagebox.showerror("Error","Complete todos los campos de tarjeta.")
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

# ======== INTERFAZ =========
root = tk.Tk()
root.title("💳 Sistema de Pagos Interactivo")
root.geometry("600x700")
root.configure(bg="#f0f4ff")  # Fondo claro y moderno

# --- Sección superior ---
frm = ttk.Frame(root, padding=15)
frm.pack(fill="x", pady=10)

metodo_var = tk.StringVar()
metodo_var.trace("w", actualizar_campos)

# --- Campos principales ---
ttk.Label(frm, text="Método de pago:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5)
combo = ttk.Combobox(frm, textvariable=metodo_var,
                     values=["Tarjeta de Crédito", "PayPal", "Efectivo", "Yape"], state="readonly", width=25)
combo.grid(row=0, column=1, padx=5, pady=5)
combo.set("Tarjeta de Crédito")

ttk.Label(frm, text="Monto (S/.):").grid(row=2, column=0, padx=5, pady=5)
entry_1 = ttk.Entry(frm, width=28)
entry_1.grid(row=2, column=1, padx=5, pady=5)

# --- Campos dinámicos ---
lbl_2, lbl_3, lbl_4, lbl_5 = [ttk.Label(frm) for _ in range(4)]
entry_2, entry_3, entry_4, entry_5 = [ttk.Entry(frm, width=28) for _ in range(4)]

# --- Botón principal ---
style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 11, "bold"), padding=6)
ttk.Button(frm, text="💰 Realizar Pago", style="Custom.TButton", command=realizar_pago).grid(
    row=8, column=0, columnspan=2, pady=15
)

# --- Área del baucher ---
frame_ticket = ttk.LabelFrame(root, text="🧾 Baucher Generado", padding=10)
frame_ticket.pack(fill="both", expand=True, padx=20, pady=10)

text_ticket = tk.Text(frame_ticket, width=70, height=20, state="disabled", bg="white", fg="black", font=("Courier", 10))
text_ticket.pack(pady=10)

# --- Inicialización ---
actualizar_campos()

root.mainloop()




