import numpy as np

edadesEmpresa2 = np.array([[34,25,16,32],[34,13,76,76]])
print(edadesEmpresa2)
print("Numero de filas",len(edadesEmpresa2))
print("Numero de columnas",len(edadesEmpresa2[0]))


a = np.array([[3,12,55,1,3],[1,9,6,1,6],[4,1,2,2,5],[7,5,4,4,1]])
print("suma total", np.sum(a))

# Sumar filas

print("Suma de filas", np.sum(a, axis = 1))

#Sumar columnas

print("Suma de columnas",np.sum(a, axis = 0)) 

#Trasponer
print("La trasposición de la matriz es ","\n", a.transpose())
