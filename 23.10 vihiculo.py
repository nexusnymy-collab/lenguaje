class vihiculoterrestre:
    def conducir(self):
        print("conduciendo por la carretera")
    def frenar(self):
        print("el vihiculo terrestre se ha detenido")

class vehiculoacuatico:
    def navegar(self):
        print("navegando por el agua")
    def fondear(self):
        print("el vihiculo acuatico ha fondeado")

class vihiculoanfibio(vihiculoterrestre,vihiculoacuatico):
    def transformar(self,modo):
        if modo=="tierra":
            print("cambiando al modo terrestre.")
        elif modo=="agua":
            print("cambiando al modo acuatico")
        else:
            print("modo no reconocido")

def main():
    anfibio=vihiculoanfibio()
    anfibio.transformar("terrestre")
    anfibio.conducir()
    anfibio.frena()

    print("\n")

    anfibio.transformar("agua")
    anfibio.navegar()
    anfibio.fondear()
if __name__=="__main__":
    main()
    
    
