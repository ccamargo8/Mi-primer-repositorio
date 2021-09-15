#Estructuras de datos

#Listas

# lista_1=['a','c','Hello',18,True]
# print(lista_1)
# longitud=len(lista_1)
# print(lista_1[0])
# print(f"Longitud de la lista: {longitud}")

#Elabore programa en Python que le permita al usuario ingresar números enteros de manera indefinida, hasta que ingrese un número negativo, y al final imprimir la suma de los números enteros pares sin incluir el número negativo en la suma.

# num=int(input("Ingrese un numero entero: "))
# suma=0
# while num>0:
#     if num % 2 == 0:
#         suma += num
#         num=int(input("Ingrese un numero entero: "))
#     else:
#         num=int(input("Ingrese un numero entero: "))
# print(suma)

# indato=True
# edad=0

# while indato==True:
#     indato=int(input("Por favor seleccione 1 para ingresar datos o cualquier numero para salir: "))
#     if indato==1:
#         indato=True
    
#         edad=int(input("Ingrese la edad: "))
#         print(f"usted ingreso: {edad}")
    
#     else:
#         indato=False
#         print("Saliendo del sistema...")

# tsa = 0.
# tau = 0.
# tns = 0.
# contador = 0
# nombre = input("entre nombre ")
# while nombre != "":
#     salario = int(input(f"{nombre} entre salario "))
#     tsa = tsa + salario
#     contador = contador + 1
#     aumento = 0.
#     if salario < 1000:
#         aumento = salario * 0.1
# tau = tau + aumento
# nuevoSalario = salario + aumento
# tns = tns + nuevoSalario
# print("Nombre", nombre, "\tsalario", salario, "\tAumento\t", aumento, "\tNuevo salario\t",

#                    nuevoSalario)
# nombre = input("entre nombre ")
# print("Total empleados", contador)
# print("Total salarios anteriores ", tsa)
# print("Total aumentos ", tau)
# print("Total nuevos salarios ", tns)

# n = int(input("Ingrese un numero entero: "))
# suma=0
# i=1

# while i<=n:
#     suma=suma+i
#     i=i+1
# print("La suma de los enteros desde 1 hasta",n,"es",suma)

# factorial=1
# i=1

# while i<=n:
#     factorial=factorial*i
#     i=i+1
# print(f"El factorial de {n} es {factorial}")

# nombre=input("Ingrese el nombre del empleado: ")
# while nombre!="":
#     salario=int(input(f"{nombre}, por favor ingrese su salario: "))
#     aumento=0.
#     if salario<1000:
#         aumento=salario*0.1
#     nuevosalario=salario+aumento
#     print("Nombre:",nombre, "\tSalario:",salario,"\tNuevo Salario:",nuevosalario,"\t Aumento:",aumento)


# Determinar si x es primo o no    
# x = int(input("Ingrese un numero entero:"))
# i=2
# while i <= x**(.5) and x % i !=0:
#     i=i+1
# if i > x**(.5):
#     print(x, "Es primo")
# else:
#     print(x,"No es primo, es divisible por",i)
    
# n = input("muestra los primos desde 3 hasta 33")
# x=3

# while x <=33:
#     i=2
#     while i <= x**(.5) and x % i !=0:
#         i=i+1
#     if i > x**(.5):
#         print(x, "Es primo")
#     x=x+2
    
# a = input("entre un número ")
# b = input("entre otro número ")
# c = int(input("entre un tercer número "))
# d = int(input("entre un cuarto número "))

# if  b > a:

#     print(c+d, end=",")
    
#     print(a+b)

# else:
#     if a == b:          

#         print(a, d)

#     else:

#         print(a, b, c, d, sep ="")

#Ciclo For para determinar si x es primo o no    
# x = int(input("Ingrese un numero entero:"))
# if x%2==0:
#     print(x,"No es primo, es par")
#     exit(0)
# i=2
# for i in range(3,int(x**(.5))+1,2):
#     if x%i==0:
#         print(x,"NO es primo, es divisible por",i)
#         break
# if x%i!=0:
#     print(x,"Es un numero primo")

n = int(input("Ingrese un numero entero "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print("")
print("")        
        
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")
print("")   

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print("")
print("")    

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print("")
print("")      
        