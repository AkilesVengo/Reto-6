def area_rectangulo(a : float, b : float) -> float:
    area_r = a*b
    return area_r

def area_circulos(r : float) -> float:
    import math
    area_c = math.pi*(r**2)*2 ##son dos círculos y por eso el 2 del final
    return area_c

def perimetro_rectangulo(a, b) -> float:
    perimetro_r = (a*2)+(b*2)
    return perimetro_r

def perimetro_circulos(r) -> float:
    import math
    perimetro_c = 2*math.pi*r*2 ##son dos círculos y por eso el 2 del final
    return perimetro_c

if __name__ == "__main__":
    a = float(input("Ingrese la altura del rectángulo:"))
    b = float(input("Ingrese el largo del rectángulo: "))
    r = float(input("Ingrese el radio que será igual para los dos círculos: "))
    area1 = area_rectangulo(a, b)
    area2 = area_circulos(r)
    perimetro1 = perimetro_rectangulo(a, b)
    perimetro2 = perimetro_circulos(r)
    print("El área del rectángulo es " +str(area1))
    print("El perímetro del rectángulo es " +str(perimetro1))
    print("El área de los dos círculos es " +str(area2))
    print("El perímetro de los dos círculos es " +str(perimetro2))