class paciente:
    def __init__(self,nombre,dni):
        self.nombre=nombre
        self.dni=dni

class cita:
    def __init__(self,paciente,fecha,especialidad):
        self.paciente=paciente
        self.fecha=fecha
        self.especialidad=especialidad

    def mostrar_informacion(self):
        print(f"paciente:{self.paciente.nombre} DNI:{self,paciente.dni}fecha{self.fecha}especialidad{self.especialidad}")

class consultorio:
    def __init__(self):
        self.citas=[]
    def agentar_cita(self,nombre,dni,fecha,especialidad):
        paciente=paciente(nombre,dni)
        cita=cita(paciente,fecha,especialidad)
        self.citas.append(cita)
        print("cita agentada correctamente")
    def mostrar_citas(self):
        if not self.citas:
            print("no hay citas agentadas")
        else:
            print("\nlista de citas agentadas")
            for cita in self.citas:
                cita.mostrar_informacion()
    def cancelar_cita(self,dni,fecha):
        for cita in self.citas:
            if cita.paciente.dni==cita.fecha==fecha:
                self.citas.remove(cita)
                print(f"cita del paciente {cita.paciente.nombre}cancelado")
                return
            print("cita no encontrada")
consultorio=consultorio()

while True:
    print("\n===== menu del consultorio=====")
    print("1.agentar cita")
    print("2.mostrar todas las citas")
    print("3. cancelar citar")
    print("4. salir")

    opcion=input("seleccione una opcion")
    if Opcion=="1":
        nombre=input("nombre del paciente:")
        dni=input("DNI del paciente")
        fecha=input("fecha de la cita{DD/MM/AAAA}")
        especialidad=input("especialidad medica")
        consultorio.agentar_cita(nombre,dni,fecha,especialidad)
    elif opcion=="2":
        consultorio.mostrar_citas()
    elif opcion=="3":
        dni=input("DNI del paciente:")
        fecha=input("fecha de la cita a cancelar {DD/MM/AAAA}:")
    elif opcion=="4":
        print("saliendo del sistema de citas medicas.")
        break
    else:
        print("opcion no valida-intenta de nuevo")
        
    
