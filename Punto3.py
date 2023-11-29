gallina : int = 6
gallo : int = 7
pollito : int = 1
def cantidad_carne(n : int, m : int, k : int) -> int:
    carne_gallina = n*gallina
    carne_gallo = m*gallo
    carne_pollito = k*pollito
    carne_total = carne_gallina+carne_gallo+carne_pollito
    return carne_total

if __name__ == "__main__":
    n = int(input("Ingrese una cantidad de gallinas: "))
    m = int(input("Ingrese una cantidad de gallos: "))
    k = int(input("Ingrese una cantidad de pollitos: "))
    carne = cantidad_carne(n, m, k)
    print("La cantidad de carne que se tiene entre gallinas, gallos y pollitos es " +str(carne)+ " Kg")