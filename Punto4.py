p_pan: int =300
p_lec: int=3300
p_hue: int=350

#Se definieron de los precios del pan, leche y huevos, como constantes

import math as m #importar libreria math

def vueta_mama(panes:float, leche:float, huevos:float, dinero:float) -> float:
  vueltas_ = (dinero- (panes*p_pan + leche*p_lec + huevos*p_hue))
  return vueltas_


if __name__ == "__main__":
  panes = float(input("Cantidad de pan:"))
  leche = float(input("Bolsas de leche:"))
  huevos = float(input("Cantidad de huevos:"))
  dinero = float(input("Cuanto dinero te dio tu mama: "))
  total_vueltas = vueta_mama(panes, leche, huevos, dinero)
  if total_vueltas > 0:
    print("La cantidad de dinero que sobro fue " +str(total_vueltas)+ " pesos")
  elif total_vueltas ==0:
    print("No te quedo dinero")
  elif total_vueltas < 0:
    total_vueltas = total_vueltas*(-1)
    print("debes" +str(total_vueltas))  