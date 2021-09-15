#Funciones

def imprimir ():
    """ Esta funcion se utiliza para imprimir. Triplecomillas se llaman DOCSTRING """ 
    print("Función para imprimir")
    print("Otro Letrero")

imprimir()
help(imprimir) #Permite imprimir lo que se ponga entre triple comillas

def imprimir_2(letrero):
    print(letrero)
    

imprimir_2("Bienvenidos")

"""Funcion que retorne el cuadrado de un numero"""

numeroglobal=20

def cuadrado(numero,numero2):
    """Funcion para calcular el cuadrado de un numero"""
    global numeroglobal #Se usa para tomar el valor de una variable global (externa)
    cuadrado=numero**2 #Variable interna. No se puede cambiar externamente
    cuad2=numero2**2
    numeroglobal=numeroglobal*2
    return cuadrado,cuad2
    
var,var1 = cuadrado(10,20)

print(var,var1,numeroglobal)

#Ejemplo de area de circulo y volumen de cilindro

PI = 3.1416

def area_circulo(radio):
    global PI
    area=PI*(radio**2)
    return area
def vol_cilindro(radio,altura):
    global PI
    volumen=area_circulo(radio)*altura
    return volumen

radio=int(input("Ingrese radio: "))
altura=int(input("Ingrese altura: "))

volumen=vol_cilindro(radio,altura)
area=area_circulo(radio)

print(f"Volumen= {volumen} \nArea={area}")

#Ejemplo calcular combinaciones posibles de un equipo de baloncesto. Forma 1
def factorial(n):
    """Funcion que ayuda a calcular el factorial de un numero"""
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(input("Ingrese el valor de n: "))
r=int(input("Ingrese el valor de r: "))

fn=factorial(n)
fr=factorial(r)
fnr=factorial(n-r)

nc=fn//fr//fnr

print("n=",n,"r=",r,"Factorial de n=",fn,"Factorial de r=",fr,"factorial n-r=",fnr,"Numero de combinaciones posibles:",nc)

#Calcular combinaciones posibles de un equipo de baloncesto importando la función desde otro archivo

import misFunciones

n=int(input("Ingrese el valor de n: "))
r=int(input("Ingrese el valor de r: "))

fn=misFunciones.factorial(n)
fr=misFunciones.factorial(r)
fnr=misFunciones.factorial(n-r)

nc=fn//fr//fnr

print("n=",n,"r=",r,"Factorial de n=",fn,"Factorial de r=",fr,"factorial n-r=",fnr,"Numero de combinaciones posibles:",nc)

#Calcular combinaciones posibles de un equipo de baloncesto importando la función desde otro archivo y asignandole un atajo al nombre del archivo de la función

import misFunciones as mf

n=int(input("Ingrese el valor de n: "))
r=int(input("Ingrese el valor de r: "))

fn=mf.factorial(n)
fr=mf.factorial(r)
fnr=mf.factorial(n-r)

nc=fn//fr//fnr

print("n=",n,"r=",r,"Factorial de n=",fn,"Factorial de r=",fr,"factorial n-r=",fnr,"Numero de combinaciones posibles:",nc)