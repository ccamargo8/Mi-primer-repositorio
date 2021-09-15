import math
import random

def factorial(n):
    """Funcion que ayuda a calcular el factorial de un numero"""
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def esPrimo(n):
    """Funcion para determinar si un numero es primo"""
    if n%2==0:
        return False    
    i=3
    while i <= math.sqrt(i):
        if n%i==0:
            return False            
        i=i+2
    return True   

def comienzaCon(x):
    """Función para determinar cual es el primer valor de un numero"""
    pd=x
    while pd>9:
        pd=pd//10
    return pd

def mcd(x,y):
    """Función para determinar el maximo comun divisor entre dos numeros"""
    res = x%y
    while res !=0:
        x=y
        y=res
        res=x%y
    return y

def mcm(x,y):
    """Función para determinar el minimo comun multiplo entre dos numeros"""
    return x*y//mcd(x,y)

def lista_aleatoria(num1,num2):
    lon=int(input("Ingrese el tamaño de la lista: "))
    lista=[None]*lon
    for i in range(lon):
        lista[i]=random.randint(num1,num2)
    return lista


    