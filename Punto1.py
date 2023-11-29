import math

def calcularVolumen(radioEsfera:float, radioCono:float, alturaCono:float) -> float:
   volumenEsfera = (4/3) * (radioEsfera**3) * math.pi
   volumenCono = (alturaCono/3) * (radioCono**2) * math.pi
   return volumenEsfera + volumenCono    

def calcularArea(radioEsfera:float, radioCono:float, alturaCono:float) -> float:
   areaEsfera = 4 * math.pi * radioEsfera**2
   alturaOblicua = math.sqrt(alturaCono*2 + radioCono*2)
   areaCono = (math.pi * radioCono * alturaOblicua) + (math.pi * radioCono**2)
   return areaEsfera + areaCono

if __name__ == '__main__':
   radioEsfera = float(input("Ingrese el radio de la esfera en cm: "))
   radioCono = float(input("Ingrese el radio del cono en cm: "))
   alturaCono = float(input("Ingrese la altura del cono en cm: "))
   volumen = calcularVolumen(radioEsfera, radioCono, alturaCono)
   area = calcularArea(radioEsfera, radioCono, alturaCono)
 
   print("El volumen de la figura es: " + str(volumen) + " cm^3")
   print("El área de la figura es: " + str(area) + " cm^2")