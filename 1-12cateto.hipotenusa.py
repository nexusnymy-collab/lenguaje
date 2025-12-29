from typing import typeVar
import math

T=typeVar('T',int,float)

def calcular_hipotenusa(cateto_a:T,cateto_b:T)->T:
    return math.sqrt(cateto_a**2+cateto_B**2)



print("hipotenusa=",calcular_hipotenusa(3,4))
print("hipotenusa=",calcular_hipotenusa(5,5,2,2))
