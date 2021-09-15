f = int(input("Cuantas empresas? "))
c = int(input("Cuantos empleados por empresa? "))
matriz=[[0]*c for i in range (f)]

print(matriz)

for i in range(f):
    suma=0
    for j in range(c):
        valor = int(input(f"Ingrese el valor para la empresa {i}, empleado{j}: "))
        matriz[i][j]=valor
        suma=suma+matriz[i][j]
    promedio=suma/c
    print(f"El promedio de la empresa {i} es {promedio}")
        
print(matriz)

#%%

def calcularPromedio(empresas):
    suma = 0
    for i in empresas:
        suma=suma+i
    return suma/len(empresas)
        

f = int(input("Cuantas empresas? "))
c = int(input("Cuantos empleados por empresa? "))
matriz=[[0]*c for i in range (f)]

print(matriz)

for i in range(f):
    suma=0
    for j in range(c):
        valor = int(input(f"Ingrese el valor para la empresa {i}, empleado{j}: "))
        matriz[i][j]=valor
        suma=suma+matriz[i][j]

for i in range(f):
    print("Empresa",i)
    x = calcularPromedio(matriz[i])
    print("Edad promedio",x)
   
        
print(matriz)