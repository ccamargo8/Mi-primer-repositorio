import numpy as np

matriz=[[1,0],[2,3]]

matriz=np.array(matriz)

Matriz_aleatoria=np.random.rand(1,10,(3,3))

x=np.array([[10,8],[9,10]])
y=np.array([[2,4],[3,2]])

#%%
print("Suma elemento a elemento de las matrices: ")
print(np.add(x,y))
#%%
print("resta elemento a elemento de las matrices: ")
print(np.subtract(x,y))
#%%
print()
print("División elemento a elemento de las matrices: ")
print(np.divide(x,y))
#%%
print()
print("multiplicacion elemento a elemento de las matrices: ")
print(np.multiply(x,y))
#%%
print()
print("multiplicacion de matrices: ")
print(np.dot(x,y))
