#Ejemplo Funciones: aplicación que calcule e imprima la hipotenusa de un triangulo rectangulo dados su catetos
def hipotenusa(a,b):
    x=(a**2+b**2)**(1/2)
    return x

while True:
    a=float(input("Ingrese el cateto 1: "))
    b=float(input("Ingrese el cateto 2: "))
    c=hipotenusa(a,b)
    print(c)
    option=input("Desea continuar? (s/n): ")
    if option=="n": break
 
