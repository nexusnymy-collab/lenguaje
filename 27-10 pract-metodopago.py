# --- Clase base ---
class MetodoPago:
    def __init__(self, monto):
        self.monto = monto

    def pagar(self):
        """Método genérico (se sobreescribe en las subclases)"""
        print(f"Procesando pago de S/. {self.monto:.2f}")

# --- Subclases específicas ---
class TarjetaCredito(MetodoPago):
    def __init__(self, monto, numero_tarjeta):
        super().__init__(monto)
        self.numero_tarjeta = numero_tarjeta

    def pagar(self):
        print(f"💳 Pago de S/. {self.monto:.2f} realizado con Tarjeta de Crédito ({self.numero_tarjeta[-4:]})")

class PayPal(MetodoPago):
    def __init__(self, monto, correo):
        super().__init__(monto)
        self.correo = correo

    def pagar(self):
        print(f"🌐 Pago de S/. {self.monto:.2f} realizado con PayPal ({self.correo})")

class Efectivo(MetodoPago):
    def pagar(self):
        print(f"💵 Pago de S/. {self.monto:.2f} realizado en efectivo")

class Yape(MetodoPago):
    def __init__(self, monto, numero):
        super().__init__(monto)
        self.numero = numero

    def pagar(self):
        print(f"📱 Pago de S/. {self.monto:.2f} realizado con Yape al número {self.numero}")

# --- Función polimórfica ---
def procesar_pago(metodo_pago):
    metodo_pago.pagar()

# --- Ejemplo de uso ---
if __name__ == "__main__":
    pagos = [
        TarjetaCredito(250.00, "1234 5678 9012 3456"),
        PayPal(180.50, "usuario@gmail.com"),
        Efectivo(75.00),
        Yape(40.00, "987654321")
    ]

    for pago in pagos:
        procesar_pago(pago)
