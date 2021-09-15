import random


estrella="\u2605"

filas=int(input("Ingrese el numero de filas: "))
columnas=int(input("Ingrese el numero de columnas: "))

#Matriz construida por comprensión
cielo=[[" " for i in range(columnas)] for j in range (filas)]

for i in range(filas): #Se recorren filas
    for j in range(columnas): #Se recorre la parte interna de cada fila       
        num=random.randint(0,5)
        if num ==2:
            cielo[i][j]=estrella

for fil in cielo:
    for elementos in fil:
        print(elementos, end=" ")
    print()    